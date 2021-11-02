from enum import Enum

class SchoolType(Enum):
    Intelligence = 0
    Artistic = 1
    Social = 2

class School:

    def __init__(self, name, school_type):
        self.__name = name
        self.__school_type = school_type

    @property
    def name(self):
        return self.__name

    @property
    def school_type(self):
        return self.__school_type


    

    