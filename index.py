"""Index module to create instances of each class"""
from animals import Alligator, Iguana, Millipede, Salamander, Snake
from animals import Dolphin, Fish, Shark, Stingray, Whale
from animals import Cow, Donkey, Goat, Horse, Llama, Goose
from attractions import PettingZoo, SnakePit, Wetlands

big_brutus = Alligator("Big Brutus", "American Alligator", "small fish", 11)
rango = Iguana("Rango", "Green Iguana", "leaves", 12)
milhouse_van_houten = Millipede("Milhouse Van Houten", "Giant African Millipede", "leaves", 13)
tiny_sally = Salamander("Tiny Sally", "Fire Salamander", "worms", 14)
david_bowie = Snake("David Bowie", "Boa Constrictor", "mice", 15)

mrs_bubbles = Dolphin("Mrs. Bubbles", "Common Bottlenose", "shrimp", 21)
nemo = Fish("Nemo", "Clownfish", "algae", 22)
bruce = Shark("Bruce", "Megalodon", "small fish", 23)
pointy_butt = Stingray("Pointy Butt", "Manta Ray", "crabs", 24)
free_willie = Whale("Free Willie", "Orca", "zooplankton", 25)

baby_bell = Cow("Baby Bell", "Domestic Cow", "Morning", "grass", 31)
little_allen = Donkey("Little Allen", "Domestic Donkey", "Midday", "carrots", 32)
black_phillip = Goat("Black Phillip", "Domestic Goat", "Afternoon", "hay", 33)
prince_charles = Horse("Prince Charles", "Domestic Horse", "Morning", "carrots", 34)
miss_fuzz = Llama("Miss Fuzz", "Domestic Llama", "Midday", "grass", 35)
bob = Goose("Bob", "Canadian Goose", "Morning", "watercress sandwiches", 36)

varmint_village = PettingZoo("Varmint Village", "cute and fuzzy critters to cuddle")
varmint_village.add_animal(baby_bell)
varmint_village.add_animal(little_allen)
varmint_village.add_animal(black_phillip)
varmint_village.add_animal(prince_charles)
varmint_village.add_animal(miss_fuzz)
varmint_village.add_animal(bob)

slither_inn = SnakePit("Slither Inn", "stupendous snakes of all sizes")
slither_inn.add_animal(big_brutus)
slither_inn.add_animal(rango)
slither_inn.add_animal(milhouse_van_houten)
slither_inn.add_animal(tiny_sally)
slither_inn.add_animal(david_bowie)

world_at_sea = Wetlands("World At Sea", "the ocean's massive, ancient collection")
world_at_sea.add_animal(mrs_bubbles)
world_at_sea.add_animal(nemo)
world_at_sea.add_animal(bruce)
world_at_sea.add_animal(pointy_butt)
world_at_sea.add_animal(free_willie)

# for animal in slither_inn.animals:
#     print(f'You can find {animal.name} the {animal.species} in {slither_inn.attraction_name}')

# varmint_village.add_animal_pythonic(miss_fuzz)
# varmint_village.add_animal_type_check(miss_fuzz)
# slither_inn.add_animal_pythonic(rango)
# slither_inn.add_animal_pythonic(bob)

# for animal in varmint_village.animals:
#     print(animal)
