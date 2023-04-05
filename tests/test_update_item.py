from db.memory import db
import uuid


def test_update_item_valid(reset_db, client):
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
    assert db.data[0].checked == True


def test_update_item_no_body(reset_db, client):
    post_response = client.post(
        "/items/",
        json={
            "title": "Test item",
        },
    )
    response = client.put(
        "/items/" + post_response.json()["item"]["id"],
        json={},
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": {"message": "Error updating item", "error": "No data to update"}
    }
    assert db.data[0].updated_at == None
    assert db.data[0].position == 1
    assert db.data[0].title == "Test item"
    assert db.data[0].checked == False


def test_update_item_invalid_id(reset_db, client):
    post_response = client.post(
        "/items/",
        json={
            "title": "Test item",
        },
    )
    response = client.put(
        "/items/" + "00000000-0000-0000-0000-000000000000",
        json={
            "title": "Test item updated",
            "checked": True,
        },
    )

    assert response.status_code == 404
    assert response.json() == {
        "detail": {"message": "Error updating item", "error": "Item not found"}
    }
    assert db.data[0].updated_at == None
    assert db.data[0].position == 1
    assert db.data[0].title == "Test item"
    assert db.data[0].checked == False

    response = client.put(
        "/items/" + "random_string",
        json={
            "title": "Test item updated",
            "checked": True,
        },
    )

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["path", "item_id"],
                "msg": "value is not a valid uuid",
                "type": "type_error.uuid",
            }
        ]
    }
    assert db.data[0].updated_at == None
    assert db.data[0].position == 1
    assert db.data[0].title == "Test item"
    assert db.data[0].checked == False
