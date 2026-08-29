from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class DocumentCreate(BaseModel):

    title: str = Field(
        min_length=1,
        max_length=255,
    )

    content: str = Field(
        min_length=1,
        max_length=10000,
    )


class DocumentResponse(BaseModel):

    id: UUID
    owner_id: UUID
    title: str
    content: str

    model_config = ConfigDict(
        from_attributes=True,
    )