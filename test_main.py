from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_quote():
    response = client.get("/quote")
    assert response.status_code == 200
    assert "quote" in response.json()
