

class Database():
    def __init__(self):
        self.data = []

    def list(self):
        return self.data
    
    def add(self, item):
        self.data.append(item)

    def remove(self, id):
        self.data = { item for item in self.data if item['id'] != id }

db = Database()