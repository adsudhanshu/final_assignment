from app.models import Leave, LeaveRequest
from app.schemas import LeaveCreate, LeaveRequestCreate
from app.utils import generate_token

class LMSservice:
    def apply_for_leave(self, leave_data: LeaveCreate):
        leave = Leave(**leave_data.dict())
        db.session.add(leave)
        db.session.commit()
        return leave

    def retrieve_leave_status(self, leave_id: int):
        leave = Leave.query.get(leave_id)
        if leave:
            return leave.status
        return None

    def approve_or_reject_leave_request(self, leave_request_id: int, status: str):
        leave_request = LeaveRequest.query.get(leave_request_id)
        if leave_request:
            leave_request.status = status
            db.session.commit()
            return leave_request
        return None