from ...core.repository import Add, Update, Remove
from ...domain.ingredients.ingredients import Ingredients


class IngredientRepo(Add, Update, Remove):
    def __init__(self, data: set[Ingredients]):
        super().__init__(data)

    # apply a filter and get the indicated page and the num of elements in the page.
    def query(self, predicate, page=0, size=10):
        filtered_data = filter(predicate, self._data)
        listed_data = list(filtered_data)
        start = page * size
        end = (page + 1) * size
        return listed_data[start:end]


ingredient_repository = IngredientRepo(set())

__all__ = ['ingredient_repository']