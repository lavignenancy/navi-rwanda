from fastapi import FastAPI

from app.api.routes.assistant import router as assistant_router
from app.api.routes.services import router as services_router
from app.api.routes.auth import router as auth_router

app = FastAPI(
    title="NAVI API",
    description=(
        "A digital companion that helps people navigate "
        "complex digital services."
    ),
    version="0.1.0",
)


app.include_router(assistant_router)
app.include_router(services_router)
app.include_router(auth_router)


@app.get("/health")
async def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "navi-api",
    }


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "message": "Welcome to NAVI",
    }