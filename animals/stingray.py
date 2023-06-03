from movements import Swimming
from .animal import Animal

class Stingray(Animal, Swimming):
    """Class to define stingrays"""
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)