from pydantic import BaseModel

class TileResponse(BaseModel):
    id: int
    title: str
    content: str
    user_role: str