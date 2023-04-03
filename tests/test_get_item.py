from db.memory import db


def test_list_items(reset_db, client):
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
