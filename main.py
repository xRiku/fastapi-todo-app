from fastapi import FastAPI
from pydantic import BaseModel, Field
from db.memory import db
from id_generator import IDGenerator
from datetime import datetime
from models.item import Item

app = FastAPI()
id_generator = IDGenerator()


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