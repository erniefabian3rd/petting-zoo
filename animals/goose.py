# The package syntax is what allows for these clean import statements
from movements import Walking, Swimming
from .animal import Animal

class Goose(Animal, Walking, Swimming):
    """Class to define geese"""
    def __init__(self, name, species, shift, food, chip_num):
        # No more super() when initializing multiple base classes
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)
        # no more self.swimming = True
        self.shift = shift

    def honk(self):
        print("The goose honks. A lot")

    # run is defined in the Walking parent class, but also here. This run method will take precedence and Walking's run method will not be called by Goose instances
    def run(self):
        print(f'{self} waddles')

    def __str__(self):
        return f'{self.name} the Goose'