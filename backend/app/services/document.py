from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.document import Document
from app.repositories.document import document_repository
from app.schemas.document import DocumentCreate


def create_document(
    db: Session,
    user_id: UUID,
    request: DocumentCreate,
) -> Document:

    document = Document(
        owner_id=user_id,
        title=request.title,
        content=request.content,
    )

    return document_repository.create(
        db,
        document,
    )


def get_document(
    db: Session,
    document_id: UUID,
    user_id: UUID,
) -> Document:

    document = document_repository.get_owned_document(
        db,
        document_id,
        user_id,
    )

    if document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found.",
        )

    return document