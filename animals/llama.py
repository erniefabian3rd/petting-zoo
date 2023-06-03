from movements import Walking
from .animal import Animal

class Llama(Animal, Walking):
    """Class to define llamas"""
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift

    def feed(self):
        print(f'{self.name} was fed {self.food} after being sung to')