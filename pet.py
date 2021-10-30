from enum import Enum
from interfaces import NamedEntity

class Gender(Enum):
    Boy = 1
    Girl = 2

class ProgressBar:

    def __init__(self, max_value):
        self.value = 0
        self.max_value = max_value

    def change(self, value):
        self.value += value
        self.value = max(self.value, 0)
        self.value = min(self.value, self.max_value)

class Pet(NamedEntity):

    def __init__(self, name, gender=random.choice(list(Gender)), generation=1):
        NamedEntity.__init__()
        self.gender = random.choice(list(Gender))
        self.age = 0
        self.weight = 0
        self.generation = generation
        self.happy = ProgressBar(4)
        self.hungry = ProgressBar(4)
        self.training = ProgressBar(10)
        self.intelligence = 0
        self.artistic = 0
        self.social = 0
