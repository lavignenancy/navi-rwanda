from pydantic import BaseModel, Field


class AssistantRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        max_length=4000,
        description="What the user needs help with.",
    )


class AssistantResponse(BaseModel):
    message: str
    intent: str
    next_steps: list[str]
    needs_clarification: bool
    clarification_question: str | None = None