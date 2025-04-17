import pytest
from app.utils import generate_token

def test_generate_token():
    user = User(username="test_user", password="test_password")
    token = generate_token(user)
    assert token is not None