from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from jose import jwt
from pydantic import BaseModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")

class User(BaseModel):
    id: int
    username: str
    role: str

def authenticate_user(username: str, password: str):
    # Implement authentication logic here
    return User(id=1, username="john", role="employee")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = jwt.decode_token(token, Config.SECRET_KEY)
    user_id = payload.get("user_id")
    return User(id=user_id, username="john", role="employee")