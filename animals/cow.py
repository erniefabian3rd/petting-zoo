from movements import Walking
from .animal import Animal

class Cow(Animal, Walking):
    """Class to define cows"""
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift
