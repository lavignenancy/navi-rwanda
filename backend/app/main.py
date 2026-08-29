from fastapi import FastAPI

from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from app.core.security.headers import SecurityHeadersMiddleware

from app.core.rate_limit import limiter
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.assistant import router as assistant_router
from app.api.routes.services import router as services_router
from app.api.routes.auth import router as auth_router
from app.api.routes.documents import router as documents_router

app = FastAPI(
    title="NAVI API",
    description=(
        "A digital companion that helps people navigate "
        "complex digital services."
    ),
    version="0.1.0",
)

app.add_middleware(
    SecurityHeadersMiddleware,
    CORSMiddleware,
    allow_origins=[
        "*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)


app.include_router(assistant_router)
app.include_router(services_router)
app.include_router(auth_router)
app.include_router(documents_router)


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