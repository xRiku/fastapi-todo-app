from fastapi import FastAPI
from pydantic import BaseModel, Field
from db.memory import db
from id_generator import IDGenerator
from datetime import datetime

app = FastAPI()
id_generator = IDGenerator()



class Item(BaseModel):
    item_id: int = Field(default_factory=id_generator.get_next_id, editable=False) 
    title: str
    checked: bool = Field(default=False, editable=False)
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat(), editable=False)
    deleted_at: str = Field(default=None, editable=False)
    updated_at: str = Field(default=None, editable=False)

@app.get("/")
async def root():
    return db.list()

@app.post("/")
async def create_item(item: Item, status_code=201):
    try: 
        db.add(item)
        # object = { "id": id_generator.get_next_id(), **item}
        # print(object)
        return { 'message': 'Item created' }
    except Exception as e:
        print(e)
        status_code = 500
        return { 'message': 'Error creating item' }