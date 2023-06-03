from movements import Slithering
from .animal import Animal

class Iguana(Animal, Slithering):
    """Class to define iguanas"""
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)

    def feed_lizard(self):
        print(f"{self.name} was fed {self.food} after it removed it's camouflage")