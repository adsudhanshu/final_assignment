import jwt
from app.config import settings

def generate_token(user: User):
    payload = {"username": user.username, "role": user.role}
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return token