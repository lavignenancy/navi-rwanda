from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.service import Service


class ServiceRepository:

    def get_all(
        self,
        db: Session,
    ) -> list[Service]:
        statement = select(Service)

        result = db.execute(statement)

        return list(result.scalars().all())


service_repository = ServiceRepository()