from fastapi import APIRouter

from app.schemas.assistant import (
    AssistantRequest,
    AssistantResponse,
)
from app.services.assistant.engine import process_request


router = APIRouter(
    prefix="/assistant",
    tags=["Assistant"],
)


@router.post(
    "/message",
    response_model=AssistantResponse,
)
async def send_message(
    request: AssistantRequest,
) -> AssistantResponse:
    return process_request(request.message)