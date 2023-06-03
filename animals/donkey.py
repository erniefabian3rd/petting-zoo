from movements import Walking
from .animal import Animal

class Donkey(Animal, Walking):
    """Class to define donkeys"""
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift