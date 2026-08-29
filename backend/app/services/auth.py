from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security.passwords import hash_password
from app.models.user import User
from app.repositories.user import user_repository
from app.schemas.auth import RegisterRequest


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