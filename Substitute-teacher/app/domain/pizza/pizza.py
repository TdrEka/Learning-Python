import copy
from ...core.entitybase import EntityBase

class Pizza(EntityBase):
    def __init__(self, id, name, description, url, ingredients):
        super().__init__(id)  # Call parent constructor with id
        self._name = name
        self._description = description
        self._url = url
        self._ingredients = copy.deepcopy(ingredients)

    # id property is now inherited from EntityBase
    # No need to define it here anymore

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def url(self):
        return self._url

    @property
    def ingredients(self):
        return copy.deepcopy(self._ingredients)

    @property
    def price(self):
        return sum(ingredient._price for ingredient in self._ingredients) * 1.2

    @classmethod
    def create(cls, id, name, description, url, ingredients):
        #pizza.create
        return cls(id, name, description, url, ingredients)

    def update(self, name, description, url, ingredients):
        #pizza.update
        self._name = name
        self._description = description
        self._url = url
        self._ingredients = ingredients

    def add_ingredients(self, ingredient):
        #pizza.add_ingredients
        self._ingredients.add(ingredient)

    def remove_ingredients(self, ingredient):
        #pizza.remove_ingredients
        self._ingredients.remove(ingredient)