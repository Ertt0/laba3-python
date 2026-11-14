from src.classrooms.errors import DuplicateID, ObjectNotFound


class Catalog:
    def __init__(self):
        self.items = {}

    def add(self, item):
        if item.id in self.items:
            raise DuplicateID("Аудитория уже есть в каталоге")
        else:
            self.items[item.id] = item

    def get(self, item_id):
        if item_id in self.items:
            return self.items[item_id]
        else:
            raise ObjectNotFound("ID не найден в каталоге")

    def remove(self, item_id):
        if item_id in self.items:
            self.items.pop(item_id)
        else:
            raise ObjectNotFound("ID отсутствует в каталоге")

    def find_by_category(self, category):
        find_audiences = [i for i in self.items.values() if category == i.category]
        return find_audiences

    def find_by_name(self, query):
        query = query.lower()
        find_audiences = [i for i in self.items.values() if query in i.name.lower()]
        return find_audiences

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        items = sorted(self.items)
        for i in items:
            yield self.items[i]

    def __contains__(self, item_id):
        return item_id in self.items
