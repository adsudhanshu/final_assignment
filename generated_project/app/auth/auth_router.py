from fastapi import APIRouter, Depends
from auth import authenticate_user, get_current_user

router = APIRouter()

@router.post("/api/auth/login")
async def login(username: str, password: str):
    user = authenticate_user(username, password)
    if user:
        token = jwt.encode({"user_id": user.id}, Config.SECRET_KEY)
        return {"access_token": token}
    return {"error": "Invalid credentials"}