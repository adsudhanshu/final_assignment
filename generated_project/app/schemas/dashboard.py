from pydantic import BaseModel

class TileCreate(BaseModel):
    title: str
    content: str
    user_role: str