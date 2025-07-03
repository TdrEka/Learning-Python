from data import Data
from notfoundexception import NotFoundException


class Add(Data):
    def add(self, entity):
        self._data.add(entity)


class Get(Data):
    def find (self, id, message="Entity doesnt exist"):
        entity =  next((item for item in self._data if item.id == id), None)
        if entity is None:
            raise NotFoundException(message)
        return entity


class Update(Get):
    def update(self, entity):
        self._data.remove(entity)
        self._data.add(entity)


class Remove (Get):
    def remove(self, entity):
        self._data.remove(entity)