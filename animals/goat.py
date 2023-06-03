from movements import Walking
from .animal import Animal

class Goat(Animal, Walking):
    """Class to define goats"""
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift