from uuid import UUID
from db.memory import db


def test_create_item(reset_db, client):
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
    assert len(db.data) == 1
    assert db.is_inside(UUID(response.json()["item"]["id"])) == True