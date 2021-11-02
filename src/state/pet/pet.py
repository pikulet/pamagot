import random
from enum import Enum

class Gender(Enum):
    Boy = 1
    Girl = 2

class Pet:

    def __init__(self, name, generation=1, gender=random.choice(list(Gender))):
        NamedEntity.__init__()
        self.__generation = generation
        self.__gender = random.choice(list(Gender))
        self.name = name
        self.age = 0
        self.weight = 0
        self.happy = ProgressBarInt(4)
        self.hungry = ProgressBarInt(4)
        self.training = ProgressBarInt(10)
        self.intelligence = 0
        self.artistic = 0
        self.social = 0
        self.school = None
        self.job = None

    @property
    def generation(self):
        return self.generation

    @property
    def gender(self):
        return self.gender

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, age):
        self.age = age

    @property
    def weight(self):
        return self.weight

    @weight.setter
    def weight(self, weight):
        self.weight = weight

    @property
    def happy(self):
        return self.happy

    @happy.setter
    def happy(self, happy):
        self.happy = happy

    @property
    def hungry(self):
        return self.hungry

    @hungry.setter
    def hungry(self, hungry):
        self.hungry = hungry

    @property
    def training(self):
        return self.training

    @training.setter
    def training(self, training):
        self.training = training

    @property
    def intelligence(self):
        return self.intelligence

    @intelligence.setter
    def intelligence(self, intelligence):
        self.intelligence = intelligence

    @property
    def artistic(self):
        return self.artistic

    @artistic.setter
    def artistic(self, artistic):
        self.artistic = artistic

    @property
    def social(self):
        return self.social

    @social.setter
    def social(self, social):
        self.social = social

    @property
    def school(self):
        return self.school

    @school.setter
    def school(self, school):
        self.school = school
        
    @property
    def job(self):
        return self.job

    @job.setter
    def job(self, job):
        self.job = job