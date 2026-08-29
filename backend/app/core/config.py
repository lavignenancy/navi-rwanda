import os


JWT_SECRET_KEY = os.getenv(
    "JWT_SECRET_KEY",
)

if not JWT_SECRET_KEY:
    raise RuntimeError(
        "JWT_SECRET_KEY environment variable is not configured."
    )


JWT_ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30

MAX_FAILED_LOGIN_ATTEMPTS = 5

ACCOUNT_LOCKOUT_MINUTES = 15