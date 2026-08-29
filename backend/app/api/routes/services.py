from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.repositories.service import service_repository
from app.schemas.service import ServiceListResponse


router = APIRouter(
    prefix="/services",
    tags=["Services"],
)


@router.get(
    "",
    response_model=ServiceListResponse,
)
async def get_services(
    db: Session = Depends(get_db),
) -> ServiceListResponse:

    services = service_repository.get_all(db)

    return ServiceListResponse(
        services=[
            {
                "id": service.id,
                "name": service.name,
            }
            for service in services
        ]
    )