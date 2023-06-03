from datetime import date

class Animal:
    """Parent class to define animals"""
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        if isinstance(chip_num, int):
            self.__chip_number = chip_num
        else:
            raise ValueError("Chip number must be an integer")

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} the {self.species}"
    
    @property
    def chip_number(self):
        return self.__chip_number
    
    @chip_number.setter
    def chip_number(self, num):
        print("Chip number may not be changed")