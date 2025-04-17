from database import get_db
from models import Leave
from schemas import LeaveResponse

class LeaveService:
    def __init__(self, db):
        self.db = db

    def apply_for_leave(self, leave_request: LeaveRequest):
        leave = Leave(**leave_request.dict())
        self.db.add(leave)
        self.db.commit()
        return LeaveResponse.from_orm(leave)

    def get_leave_status(self, leave_id: int):
        leave = self.db.query(Leave).filter(Leave.id == leave_id).first()
        if leave:
            return LeaveResponse.from_orm(leave)
        return None