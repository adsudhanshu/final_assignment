from fastapi import APIRouter, Depends
from app.services import lms_service
from app.schemas import LeaveCreate, LeaveRequestCreate

router = APIRouter()

@router.post("/apply")
async def apply_for_leave(leave_data: LeaveCreate):
    leave = lms_service.apply_for_leave(leave_data)
    return {"id": leave.id}

@router.get("/status")
async def retrieve_leave_status(leave_id: int):
    status = lms_service.retrieve_leave_status(leave_id)
    return {"status": status}

@router.patch("/approve/{leave_request_id}")
async def approve_or_reject_leave_request(leave_request_id: int, status: str):
    leave_request = lms_service.approve_or_reject_leave_request(leave_request_id, status)
    return {"id": leave_request.id}