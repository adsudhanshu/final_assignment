from pydantic import BaseModel
from app.models import Leave, LeaveRequest

class LeaveCreate(BaseModel):
    start_date: str
    end_date: str
    reason: str

class LeaveRequestCreate(BaseModel):
    employee_id: int
    leave_id: int