from pydantic import BaseModel

class PodMember(BaseModel):
    pod_id: int
    employee_id: int
    role: str

class PodResponse(BaseModel):
    id: int
    name: str
    members: List[PodMember]