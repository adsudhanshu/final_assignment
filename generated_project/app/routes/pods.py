from fastapi import APIRouter, Depends
from app.services import pods_service
from app.schemas import PodCreate, PodMemberCreate

router = APIRouter()

@router.post("/assign")
async def assign_employee_to_pod(pod_data: PodCreate):
    pod = pods_service.assign_employee_to_pod(pod_data)
    return {"id": pod.id}

@router.get("/members")
async def retrieve_pod_members(pod_id: int):
    pod_members = pods_service.retrieve_pod_members(pod_id)
    return pod_members

@router.post("/recommend")
async def recommend_employees_for_pods(employee_ids: List[int]):
    pods_service.recommend_employees_for_pods(employee_ids)
    return {"message": "Employees recommended for pods"}