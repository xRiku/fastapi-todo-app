import uuid
from fastapi import APIRouter, HTTPException
from db.memory import db
from models.item import Item, ItemUpdate

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/")
async def root():
    return db.list()

@router.post("/")
async def create_item(item: Item):
    try: 
        db.add(item)
        return { 'message': 'Item created' }
    except Exception as e:
        status_code = 500
        error_message =  { 'message': 'Error creating item',  'error': str(e)}
        raise HTTPException(status_code=status_code, detail=error_message)
    
@router.put("/{item_id}")
async def update_item(item_id: uuid.UUID, item_update: ItemUpdate):
    try:
        db.update(item_id, item_update.dict(exclude_unset=True))
        return { 'message': 'Item updated' }
    except Exception as e:
        status_code = 500
        error_message =  { 'message': 'Error updating item', 'error': str(e)}
        raise HTTPException(status_code=status_code, detail=error_message)