import pytest
from app.pods.models import Pod, PodMember
from app.pods.schemas import PodCreate

@pytest.mark.usefixtures("client")
class TestPods:
    def test_assign_employee_to_pod(self, client):
        pod_data = {"name": "Pod 1", "members": [1, 2, 3]}
        response = client.post("/pods/assign", json=pod_data)
        assert response.status_code == 201
        assert response.json()["id"] is not None

    def test_retrieve_pod_members(self, client):
        response = client.get("/pods/members")
        assert response.status_code == 200
        assert len(response.json()) == 3

    def test_recommend_employees_for_pods(self, client):
        employee_ids = [4, 5, 6]
        response = client.post("/pods/recommend", json={"employee_ids": employee_ids})
        assert response.status_code == 200
        assert len(response.json()) == 3