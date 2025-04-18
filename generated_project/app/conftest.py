import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

@pytest.fixture
def authenticated_client(user):
    token = user.generate_token()
    client = TestClient(app)
    client.headers.update({"Authorization": f"Bearer {token}"})
    return client