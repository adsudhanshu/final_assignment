from database import get_db
from generated_project.app.schemas.pod import PodMember
from models import Pod
from schemas import PodResponse

class PodService:
    def __init__(self, db):
        self.db = db

    def assign_employee_to_pod(self, pod_id: int, employee_id: int):
        pod_member = PodMember(pod_id=pod_id, employee_id=employee_id)
        self.db.add(pod_member)
        self.db.commit()
        return PodResponse.from_orm(self.db.query(Pod).filter(Pod.id == pod_id).first())