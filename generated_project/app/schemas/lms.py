from pydantic import BaseModel

class LeaveRequestCreate(BaseModel):
    start_date: str
    end_date: str
    reason: str
    employee_id: int
    leave_id: int