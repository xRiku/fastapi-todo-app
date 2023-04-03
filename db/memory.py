from datetime import datetime
import uuid
from models.item import Item, id_generator


class Database:
    def __init__(self):
        self.data = []

    def is_inside(self, id: uuid.UUID) -> bool:
        return id in [item.id for item in self.data if item.deleted_at == None]

    def list_all(self, deleted_at: bool) -> list[Item]:
        if deleted_at:
            return self.data
        return [item for item in self.data if item.deleted_at == None]

    def add(self, item: Item) -> None:
        self.data.append(item)

    def update(self, id: uuid.UUID, fields: dict) -> None:
        if not self.is_inside(id):
            raise Exception("Item not found")
        for i, value in enumerate(self.data):
            if value.id == id:
                for field, new_value in fields.items():
                    setattr(self.data[i], field, new_value)
                self.data[i].updated_at = datetime.now().isoformat()

    def remove(self, id: uuid.UUID) -> None:
        if not self.is_inside(id):
            raise Exception("Item not found")
        for i, value in enumerate(self.data):
            if value.id == id:
                self.data[i].deleted_at = datetime.now().isoformat()

    def wipe(self) -> None:
        self.data = []
        id_generator.reset()


db = Database()
