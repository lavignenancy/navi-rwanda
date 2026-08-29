from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security.dependencies import get_current_user
from app.db.dependencies import get_db
from app.models.user import User
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
    current_user: User = Depends(get_current_user),
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