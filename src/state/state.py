class PamagotState:

    def __init__(self):
        self.pet = Pet()
        self.food_inventory = Inventory()
        self.item_inventory = Inventory()
        self.points = 0
        self.friend_list = FriendList()

    @property
    def pet(self):
        return self.pet

    @pet.setter
    def pet(self, pet):
        self.pet = pet

    @property
    def food_inventory(self):
        return self.food_inventory

    @property
    def item_inventory(self):
        return self.item_inventory

    @property
    def points(self):
        return self.points

    @points.setter
    def points(self, points):
        self.points = points

    @property
    def friend_list(self):
        return self.friend_list