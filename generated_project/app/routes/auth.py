from fastapi import APIRouter, Depends
from app.services import auth_service
from app.schemas import UserCreate

router = APIRouter()

@router.post("/login")
async def login(username: str, password: str):
    token = auth_service.login(username, password)
    return {"access_token": token}

@router.get("/user")
async def fetch_current_user_details(token: str):
    user = auth_service.fetch_current_user_details(token)
    return user