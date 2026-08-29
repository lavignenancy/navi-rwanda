from app.schemas.assistant import AssistantResponse


def process_request(message: str) -> AssistantResponse:
    """
    Initial NAVI reasoning layer.

    This version is intentionally deterministic.
    AI capabilities will be added behind this interface later.
    """

    text = message.strip()

    if not text:
        return AssistantResponse(
            message="I need a little more information to help you.",
            intent="unknown",
            next_steps=[],
            needs_clarification=True,
            clarification_question="What are you trying to do?",
        )

    return AssistantResponse(
        message=(
            "I understand that you need help. "
            "Let's work out what you need and what to do next."
        ),
        intent="general_request",
        next_steps=[
            "Understand what you are trying to accomplish",
            "Identify the information or documents you may need",
            "Guide you through the correct next steps",
        ],
        needs_clarification=True,
        clarification_question="What are you trying to accomplish?",
    )