from db.memory import db


def test_list_items(reset_db, client):
    _ = client.post(
        "/items/",
        json={
            "title": "Test item",
        },
    )
    response = client.get("/items/")
    items = response.json()
    assert response.status_code == 200
    assert len(items) == 1
    assert items[0]["title"] == "Test item"
    assert items[0]["checked"] is False
    assert items[0]["position"] == 1
    assert items[0]["created_at"] is not None
    assert items[0]["updated_at"] is None
    assert items[0]["deleted_at"] is None
    assert items[0]["id"] is not None
