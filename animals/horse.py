from movements import Walking
from .animal import Animal

class Horse(Animal, Walking):
    """Class to define horses"""
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift