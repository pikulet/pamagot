from pet import Pet

class NamedEntity:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Item(NamedEntity):

    @abstractmethod
     def interact_with(self, p: Pet):
         pass

~
