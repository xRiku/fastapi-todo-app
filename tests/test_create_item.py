from uuid import UUID
from db.memory import db


def test_create_item_valid(reset_db, client):
    response = client.post(
        "/items/",
        json={
            "title": "Test item",
        },
    )

    assert response.status_code == 201
    item = response.json()["item"]
    assert response.json()["message"] == "Item created"
    assert item["title"] == "Test item"
    assert item["checked"] is False
    assert item["position"] == 1
    assert item["created_at"] is not None
    assert item["updated_at"] is None
    assert item["deleted_at"] is None
    assert item["id"] is not None
    assert len(db.data) == 1
    assert db.is_inside(UUID(response.json()["item"]["id"])) == True


def test_create_item_edge(reset_db, client):
    response = client.post(
        "/items/",
        json={
            "title": "",
        },
    )

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "title"],
                "msg": "must not be blank",
                "type": "value_error",
            }
        ]
    }
    assert len(db.data) == 0


def test_create_item_no_body(reset_db, client):
    response = client.post(
        "/items/",
        json={},
    )

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "title"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
    }
    assert len(db.data) == 0


def test_create_item_forbidden_fields(reset_db, client):
    response = client.post(
        "/items/",
        json={
            "title": "Test item",
            "checked": True,
            "position": 2,
            "created_at": "2021-04-01T00:00:00",
            "updated_at": "2021-04-01T00:00:00",
            "deleted_at": "2021-04-01T00:00:00",
            "id": "00000000-0000-0000-0000-000000000000",
        },
    )

    assert response.status_code == 201
    item = response.json()["item"]
    assert response.json()["message"] == "Item created"
    assert item["title"] == "Test item"
    assert item["checked"] is False
    assert item["position"] == 1
    assert item["created_at"] is not None
    assert item["updated_at"] is None
    assert item["deleted_at"] is None
    assert item["id"] is not None
    assert len(db.data) == 1
    assert db.is_inside(UUID(response.json()["item"]["id"])) == True
