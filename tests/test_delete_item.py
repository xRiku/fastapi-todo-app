from db.memory import db


def test_delete_item(reset_db, client):
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
