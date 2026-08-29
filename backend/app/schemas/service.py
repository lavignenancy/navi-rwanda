from pydantic import BaseModel


class Service(BaseModel):
    id: str
    name: str


class ServiceListResponse(BaseModel):
    services: list[Service]