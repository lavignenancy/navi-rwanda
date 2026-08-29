from fastapi import APIRouter, Depends

from app.core.security.dependencies import get_current_user
from app.models.user import User
from app.schemas.assistant import (
    AssistantRequest,
    AssistantResponse,
)
from app.services.assistant.engine import process_request


router = APIRouter(
    prefix="/assistant",
    tags=["Assistant"],
)


@router.get(
    "/message",
    response_model=AssistantResponse,
)
async def send_message(
    request: AssistantRequest,
    current_user: User = Depends(get_current_user),
) -> AssistantResponse:

    return process_request(request.message)