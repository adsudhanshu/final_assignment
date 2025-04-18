from pydantic import BaseModel
from app.models import User

class UserCreate(BaseModel):
    username: str
    password: str
    role: str