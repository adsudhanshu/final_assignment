from pydantic import BaseModel
from app.models import Tile

class TileCreate(BaseModel):
    title: str
    content: str
    user_role: str