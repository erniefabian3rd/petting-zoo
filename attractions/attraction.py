class Attraction:
    """Parent class to define attractions"""
    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def __str__(self):
        animal_names = "\n   * ".join(str(animal) for animal in self.animals)
        return f"{self.attraction_name} is where you'll find {self.description}, like\n   * {animal_names}"

    def __len__(self):
        return len(self.animals)

    @property
    def last_critter_add(self):
        return self.animals[-1]