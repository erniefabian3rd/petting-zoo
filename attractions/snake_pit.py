from .attraction import Attraction

class SnakePit(Attraction):
    """Class to define snake pit attraction"""
    def __init__(self, name, description):
        super().__init__(name, description)

    def add_animal_pythonic(self, animal):
        try:
            if animal.slither_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError:
            print(f'{animal} will get eaten alive, so please do not put it in the {self.attraction_name} attraction.')