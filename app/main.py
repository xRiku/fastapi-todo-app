from fastapi import FastAPI
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
        print(e)
        status_code = 500
        return { 'message': 'Error creating item' }