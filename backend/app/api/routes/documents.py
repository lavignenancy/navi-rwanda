from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.security.dependencies import get_current_user
from app.db.dependencies import get_db
from app.models.user import User
from app.schemas.document import (
    DocumentCreate,
    DocumentResponse,
)
from app.services.document import (
    create_document,
    get_document,
)


router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post(
    "",
    response_model=DocumentResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_user_document(
    request: DocumentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> DocumentResponse:

    document = create_document(
        db,
        current_user.id,
        request,
    )

    return document


@router.get(
    "/{document_id}",
    response_model=DocumentResponse,
)
async def get_user_document(
    document_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> DocumentResponse:

    document = get_document(
        db,
        document_id,
        current_user.id,
    )

    return document