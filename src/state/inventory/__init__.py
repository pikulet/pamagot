from abc import abstractmethod
from state.pet import Pet

class Item:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def interact_with(self, p: Pet):
        pass

class Inventory:

    def __init__(self):
        self.items = []

    @property
    def items(self):
        return self.items
    
    def add_item(self, item):
        self.items.append(item)

    def use_item(self, index):
        return self.items.pop(index)

    def drop_item(self, index):
        self.items.pop(index)