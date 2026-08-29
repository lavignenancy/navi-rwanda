from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.auth import RegisterRequest, UserResponse
from app.services.auth import register_user


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def register(
    request: RegisterRequest,
    db: Session = Depends(get_db),
) -> UserResponse:

    user = register_user(
        db,
        request,
    )

    return UserResponse(
        id=str(user.id),
        email=user.email,
        role=user.role,
    )