from pydantic import BaseModel

class LeaveRequest(BaseModel):
    employee_id: int
    leave_id: int
    status: str

class LeaveResponse(BaseModel):
    id: int
    start_date: str
    end_date: str
    reason: str
    status: str