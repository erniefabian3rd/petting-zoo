from movements import Swimming
from .animal import Animal

class Dolphin(Animal, Swimming):
    """Class to define dolphins"""
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
    
    def feed(self):
        print(f'{self.name} was fed {self.food} after jumping through all the hoops')