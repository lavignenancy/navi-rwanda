from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(
        min_length=12,
        max_length=128,
    )


class UserResponse(BaseModel):
    id: str
    email: EmailStr
    role: str