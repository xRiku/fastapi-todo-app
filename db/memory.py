

from datetime import datetime
import uuid
from models.item import Item


class Database():
    def __init__(self):
        self.data = []

    def list(self):
        return self.data
    
    def add(self, item: Item):
        self.data.append(item)

    def update(self, id: uuid.UUID, item: Item):
        try:
            for i, value in enumerate(self.data):
                if value.id == id:
                    self.data[i] = item
                    self.data[i].updated_at = datetime.now().isoformat()
        except Exception as e:
            print(e)

    def remove(self, id: uuid.UUID):
        self.data = { item for item in self.data if item['id'] != id }

db = Database()