import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DATABASE_URL = os.environ.get("DATABASE_URL")
    JWT_TOKEN_EXPIRE_MINUTES = 30
    RATE_LIMIT = "100/minute"