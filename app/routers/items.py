import uuid
from fastapi import APIRouter, HTTPException
from db.memory import db
from models.item import Item, ItemUpdate

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/")
async def list_items(deleted_at: bool = False) -> list[Item]:
    return db.list_all(deleted_at)


@router.post("/", status_code=201)
async def create_item(item: Item) -> dict:
    try:
        db.add(item)
        return {"message": "Item created", "item": item.dict()}
    except Exception as e:
        status_code = 500
        error_message = {"message": "Error creating item", "error": str(e)}
        raise HTTPException(status_code=status_code, detail=error_message)


@router.put("/{item_id}")
async def update_item(item_id: uuid.UUID, item_update: ItemUpdate) -> dict:
    try:
        db.update(item_id, item_update.dict(exclude_unset=True))
        return {"message": "Item updated"}
    except Exception as e:
        status_code = 500
        error_message = {"message": "Error updating item", "error": str(e)}
        raise HTTPException(status_code=status_code, detail=error_message)


@router.delete("/{item_id}")
async def delete_item(item_id: uuid.UUID) -> dict:
    try:
        db.remove(item_id)
        return {"message": "Item deleted"}
    except Exception as e:
        status_code = 500
        error_message = {"message": "Error deleting item", "error": str(e)}
        raise HTTPException(status_code=status_code, detail=error_message)
