from enum import Enum

class JobType(Enum):
    Intelligence = 0
    Artistic = 1
    Social = 2

class Job:

    def __init__(self, name, job_type):
        self.__name = name
        self.__job_type = job_type

    @property
    def name(self):
        return self.__name

    @property
    def job_type(self):
        return self.__job_type


    

    