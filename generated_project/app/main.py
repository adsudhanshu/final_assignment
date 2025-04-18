from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.security.oauth2 import OAuth2PasswordBearer
from fastapi.security.utils import get_authorization_scheme_param
from starlette.status import HTTP_401_UNAUTHORIZED
from app.config import settings
from app.utils import generate_token
from app.models import User
from app.services import lms_service, pods_service, dashboard_service, auth_service

app = FastAPI(title="Leave Management System", version="1.0")

@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": str(exc)})

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Process-Time"] = str(response.headers.get("X-Process-Time", ""))
    return response

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")

@app.on_event("startup")
async def startup_event():
    await auth_service.create_admin_user()

@app.on_event("shutdown")
async def shutdown_event():
    pass