import uuid
from fastapi import FastAPI, HTTPException
from db.memory import db
from id_generator import IDGenerator
from models.item import Item

app = FastAPI()
id_generator = IDGenerator()


@app.get("/")
async def root():
    return db.list()

@app.post("/")
async def create_item(item: Item):
    try: 
        db.add(item)
        return { 'message': 'Item created' }
    except Exception as e:
        status_code = 500
        error_message =  { 'message': 'Error creating item',  'error': str(e)}
        raise HTTPException(status_code=status_code, detail=error_message)
    
@app.put("/{item_id}")
async def update_item(item_id: uuid.UUID, item: Item):
    try:
        db.update(item_id, item)
        return { 'message': 'Item updated' }
    except Exception as e:
        status_code = 500
        error_message =  { 'message': 'Error updating item', 'error': str(e)}
        raise HTTPException(status_code=status_code, detail=error_message)