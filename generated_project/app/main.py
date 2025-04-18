from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.security.oauth2 import OAuth2PasswordBearer
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.docs import get_redoc_html
from starlette.responses import RedirectResponse
from starlette.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED
from app.config import settings
from app.utils import generate_token
from app.models import User
from app.services import lms_service, pods_service, dashboard_service, auth_service

app = FastAPI(
    title="Leave Management System",
    description="Leave Management System API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": str(exc)})

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

@app.on_event("startup")
async def startup_event():
    await auth_service.create_admin_user()

@app.on_event("shutdown")
async def shutdown_event():
    pass