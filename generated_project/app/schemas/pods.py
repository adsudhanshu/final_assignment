from pydantic import BaseModel
from app.models import Pod, PodMember

class PodCreate(BaseModel):
    name: str
    members: List[int]

class PodMemberCreate(BaseModel):
    pod_id: int
    employee_id: int
    role: str