

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

    def update(self, id: uuid, title: str):
        for i, value in enumerate(self.data):
            if value['id'] == id:
                self.data[i]['title'] = title
                self.data[i]['updated_at'] = datetime.now().isoformat()

    def remove(self, id: uuid):
        self.data = { item for item in self.data if item['id'] != id }

db = Database()