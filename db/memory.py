

from datetime import datetime
import uuid
from models.item import Item


class Database():
    def __init__(self):
        self.data = []

    def is_inside(self, id: uuid.UUID) -> bool:
        return id in [item.id for item in self.data]


    def list_all(self) -> list[Item]:
        return self.data
    
    def add(self, item: Item) -> None:
        self.data.append(item)

    def update(self, id: uuid.UUID, fields: dict) -> None:
        try:
            for i, value in enumerate(self.data):
                if value.id == id:
                    for field, new_value in fields.items():
                        setattr(self.data[i], field, new_value)
                    self.data[i].updated_at = datetime.now().isoformat()
        except Exception as e:
            print(e)

    def remove(self, id: uuid.UUID) -> None:
        self.data = { item for item in self.data if item['id'] != id }

db = Database()