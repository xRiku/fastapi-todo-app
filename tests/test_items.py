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


def test_update_item(reset_db):
    post_response = client.post(
        "/items/",
        json={
            "title": "Test item",
        },
    )
    response = client.put(
        "/items/" + post_response.json()["item"]["id"],
        json={
            "title": "Test item updated",
            "checked": True,
        },
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Item updated"}
    assert db.data[0].updated_at != None
    assert db.data[0].position == 1
    assert db.data[0].title == "Test item updated"


def test_delete_item(reset_db):
    post_response = client.post(
        "/items/",
        json={
            "title": "Test item",
        },
    )
    response = client.delete("/items/" + post_response.json()["item"]["id"])

    assert response.status_code == 200
    assert response.json() == {"message": "Item deleted"}
    assert db.data[0].deleted_at != None
    assert client.get("/items/").json() == []
