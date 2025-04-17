from fastapi import APIRouter, Depends
from services import PodService
from schemas import PodResponse

router = APIRouter()

@router.post("/pods/assign")
async def assign_employee_to_pod(pod_id: int, employee_id: int, db: Session = Depends()):
    pod_service = PodService(db)
    return pod_service.assign_employee_to_pod(pod_id, employee_id)

@router.get("/pods/members")
async def get_pod_members(pod_id: int, db: Session = Depends()):
    pod_service = PodService(db)
    return pod_service.get_pod_members(pod_id)