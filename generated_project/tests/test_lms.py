import pytest
from app.lms.models import Leave, LeaveRequest
from app.lms.schemas import LeaveRequestCreate

@pytest.mark.usefixtures("client")
class TestLeaveManagementSystem:
    def test_apply_for_leave(self, client):
        leave_data = {"start_date": "2023-03-01", "end_date": "2023-03-05", "reason": "Vacation"}
        response = client.post("/leave/apply", json=leave_data)
        assert response.status_code == 201
        assert response.json()["id"] is not None

    def test_retrieve_leave_status(self, client):
        leave_request = LeaveRequestCreate(employee_id=1, leave_id=1)
        response = client.get("/leave/status")
        assert response.status_code == 200
        assert response.json()["status"] == "pending"

    def test_approve_or_reject_leave_request(self, authenticated_client, leave_request):
        response = authenticated_client.patch(f"/leave/approve/{leave_request.id}", json={"status": "approved"})
        assert response.status_code == 200
        assert response.json()["status"] == "approved"

    def test_leave_request_status_update(self, client, leave_request):
        response = client.get("/leave/status")
        assert response.status_code == 200
        assert response.json()["status"] == "approved"