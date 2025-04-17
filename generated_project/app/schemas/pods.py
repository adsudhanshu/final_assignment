from pydantic import BaseModel

class PodCreate(BaseModel):
    name: str
    members: List[int]