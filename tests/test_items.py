from fastapi.testclient import TestClient
from uuid import UUID

import pytest
from app.main import app
from db.memory import db

client = TestClient(app)


@pytest.fixture()
def reset_db():
    db.wipe()


def test_create_item(reset_db):
    db.wipe()
    response = client.post(
        "/items/",
        json={
            "title": "Test item",
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        "message": "Item created",
        "item": {
            "id": response.json()["item"]["id"],
            "title": "Test item",
            "checked": False,
            "created_at": response.json()["item"]["created_at"],
            "deleted_at": None,
            "updated_at": None,
            "position": 1,
        },
    }
    assert db.is_inside(UUID(response.json()["item"]["id"])) == True


def test_list_items(reset_db):
    assert len(db.data) == 0
    _ = client.post(
        "/items/",
        json={
            "title": "Test item",
        },
    )
    response = client.get("/items/")

    assert response.status_code == 200
    assert response.json() == [
        {
            "id": response.json()[0]["id"],
            "title": "Test item",
            "checked": False,
            "created_at": response.json()[0]["created_at"],
            "deleted_at": None,
            "updated_at": None,
            "position": 1,
        }
    ]
