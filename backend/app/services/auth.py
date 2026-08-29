from datetime import datetime, timedelta, timezone

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.config import (
    ACCOUNT_LOCKOUT_MINUTES,
    MAX_FAILED_LOGIN_ATTEMPTS,
)
from app.core.security.passwords import (
    hash_password,
    verify_password,
)
from app.core.security.tokens import create_access_token
from app.models.user import User
from app.repositories.user import user_repository
from app.schemas.auth import (
    LoginRequest,
    RegisterRequest,
)


def register_user(
    db: Session,
    request: RegisterRequest,
) -> User:

    existing_user = user_repository.get_by_email(
        db,
        request.email,
    )

    if existing_user is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Unable to create account.",
        )

    user = User(
        email=request.email,
        password_hash=hash_password(
            request.password
        ),
        role="user",
    )

    return user_repository.create(
        db,
        user,
    )


def login_user(
    db: Session,
    request: LoginRequest,
) -> str:

    user = user_repository.get_by_email(
        db,
        request.email,
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials.",
        )

    now = datetime.now(timezone.utc)

    # Check account lockout BEFORE password verification.
    if (
        user.locked_until is not None
        and user.locked_until > now
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials.",
        )

    # If the previous lockout has expired,
    # reset the login failure counter.
    if (
        user.locked_until is not None
        and user.locked_until <= now
    ):
        user.locked_until = None
        user.failed_login_attempts = 0
        db.commit()

    if not verify_password(
        request.password,
        user.password_hash,
    ):
        user.failed_login_attempts += 1

        if (
            user.failed_login_attempts
            >= MAX_FAILED_LOGIN_ATTEMPTS
        ):
            user.locked_until = (
                now
                + timedelta(
                    minutes=ACCOUNT_LOCKOUT_MINUTES
                )
            )

        db.commit()

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials.",
        )

    # Successful login.
    user.failed_login_attempts = 0
    user.locked_until = None

    db.commit()

    return create_access_token(
        user_id=str(user.id),
        role=user.role,
    )