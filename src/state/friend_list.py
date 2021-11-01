class Friend:

    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

class FriendList:

    def __init__(self):
        self.__friends: list[Friend]

    @property
    def friends(self):
        return self.__friends

    def get_friend(self, index):
        return self.__friends[index]

    def remove_friend(self, index):
        self.__friends.pop(index)