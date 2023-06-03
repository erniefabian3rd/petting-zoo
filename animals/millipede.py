from movements import Slithering
from .animal import Animal

class Millipede(Animal, Slithering):
    """Class to define millipedes"""
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)