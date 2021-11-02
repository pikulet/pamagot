from enum import Enum
    
class Species:

    def __init__(self, name, phase):
        self.name = name

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

class Baby(Species):
    pass

class Child(Species):
    pass

