from fastapi import FastAPI

from app.api.routes.assistant import router as assistant_router


app = FastAPI(
    title="NAVI API",
    description=(
        "A digital companion that helps people navigate "
        "complex digital services."
    ),
    version="0.1.0",
)


app.include_router(assistant_router)


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