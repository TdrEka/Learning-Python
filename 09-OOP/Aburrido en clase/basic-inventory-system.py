# how the fuck am i even going to go about this...
# is this really supposed to be level 1?

class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Inventory:
    def __init__(self):
        self.current_weight = 0
        self.items = {}

    def add_to_inventory(self, item, quantity = 1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
        self.current_weight += item.weight * quantity

    def drop(self, item, quantity = 1):
        if item not in self.items:
            print(f"Cannot remove {item.name}, not in inventory.")
            return
        if self.items[item] < quantity:
            print(f"Cannot remove {quantity} {item.name}s, only have {self.items[item]}.")
            return
        self.items[item] -= quantity
        self.current_weight -= item.weight * quantity
        if self.items[item] == 0:
            del self.items[item]

class Peasant:
    def __init__(self, constitution = 10):
        self.con = constitution
        self.carry_capacity = self.con * 10
        self.encumbered = False
        self.inventory = Inventory()

    def add_to_inventory(self, item, quantity = 1):
        self.inventory.add_to_inventory(item, quantity)
        self.update_encumberance()

    def drop(self, item, quantity = 1):
        self.inventory.drop(item, quantity)
        self.update_encumberance()

    def update_encumberance(self):
        weight = self.inventory.current_weight
        self.encumbered = weight > self.carry_capacity

    def __str__(self):
        status = "I'm tired boss.." if self.encumbered else "Chilling"
        return f"{status}, {self.inventory.current_weight}/{self.carry_capacity}kg"