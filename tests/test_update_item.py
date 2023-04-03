from db.memory import db


def test_update_item(reset_db, client):
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
