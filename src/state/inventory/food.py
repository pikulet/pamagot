from inventory import Item
from pet import Pet

class Food(Item):

    def __init__(self, name, calories):
        Item.__init__(name)
        self.calories = calories

    def interact_with(self, p: Pet):
        p.weight += self.calories

class Meal(Food):

    def __init__(self, name):
        Food.__init__(name, 1)

    def interact_with(self, p: Pet):
        Food.interact_with(p)
        p.hungry += 1

class Snack(Food):

    def __init__(self, name):
        Food.__init__(name, 2)

    def interact_with(self, p: Pet):
        Food.interact_with(p)
        p.happy += 1
