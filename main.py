from fastapi import FastAPI
from db.memory import db
from id_generator import IDGenerator

app = FastAPI()
id_generator = IDGenerator()

@app.get("/")
async def root():
    return db.list()

@app.post("/")
async def create_item(item: dict, status_code=201):
    try: 
        db.add({ "id": id_generator.get_next_id(), **item})
        # object = { "id": id_generator.get_next_id(), **item}
        # print(object)
        return { 'message': 'Item created' }
    except Exception as e:
        print(e)
        status_code = 500
        return { 'message': 'Error creating item' }