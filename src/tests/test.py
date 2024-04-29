from fastapi.testclient import TestClient
import pytest
from src.server import app

client = TestClient(app)

def test_is_running():
    response = client.get("/is_running")
    assert response.status_code == 200
    assert response.json() == {"running": True}

