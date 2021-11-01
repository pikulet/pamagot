from inventory import Item
from pet import Pet

class Toy(Item):

    def __init__(self, name):
        Item.__init__(name)

    def interact_with(self, p: Pet):
        p.happy += 1
