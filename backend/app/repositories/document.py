from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.document import Document


class DocumentRepository:

    def create(
        self,
        db: Session,
        document: Document,
    ) -> Document:

        db.add(document)
        db.commit()
        db.refresh(document)

        return document

    def get_owned_document(
        self,
        db: Session,
        document_id: UUID,
        owner_id: UUID,
    ) -> Document | None:

        statement = select(Document).where(
            Document.id == document_id,
            Document.owner_id == owner_id,
        )

        result = db.execute(statement)

        return result.scalar_one_or_none()


document_repository = DocumentRepository()