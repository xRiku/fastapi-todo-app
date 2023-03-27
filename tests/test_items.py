from fastapi.testclient import TestClient
from uuid import UUID
from app.main import app

client = TestClient(app)


def test_create_item():
    response = client.post(
        "/items/",
        json={
            "title": "Test item",
        },
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Item created"}

