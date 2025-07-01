from ...core.entitybase import EntityBase

class Ingredients(EntityBase):

    def __init__(self, id, name, price):
        super().__init__(id)  # Call parent constructor with id
        self._name = name
        self._price = price


    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    def update(self, id, name, price):
        # Ingredients.update
        self._id = id  # Still need to update the id if changed
        self._name = name
        self._price = price

    @classmethod
    def create(cls, id, name, price):
        # Ingredients.create
        return cls(id, name, price)