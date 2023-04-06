from db.memory import db


def test_delete_item_valid(reset_db, client):
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


def test_delete_item_invalid_id(reset_db, client):
    post_response = client.post(
        "/items/",
        json={
            "title": "Test item",
        },
    )

    response = client.delete("/items/" + "00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404
    assert response.json() == {
        "detail": {"message": "Error deleting item", "error": "Item not found"}
    }
    assert db.data[0].deleted_at == None
