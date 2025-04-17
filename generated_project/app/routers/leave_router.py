from fastapi import APIRouter, Depends
from services import LeaveService
from schemas import LeaveRequest, LeaveResponse

router = APIRouter()

@router.post("/leave/apply")
async def apply_for_leave(leave_request: LeaveRequest, db: Session = Depends()):
    leave_service = LeaveService(db)
    return leave_service.apply_for_leave(leave_request)

@router.get("/leave/status/{leave_id}")
async def get_leave_status(leave_id: int, db: Session = Depends()):
    leave_service = LeaveService(db)
    return leave_service.get_leave_status(leave_id)