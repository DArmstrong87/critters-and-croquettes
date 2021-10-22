# import the python datetime module to help us create a timestamp
from models import Snake, SwimmingAnimal, WalkingAnimal
from attractions import PettingZoo, SnakePit, Aquarium

bandit = WalkingAnimal('Bandit', 'raccoon', 'raccoon chow', 'morning')
jolene = WalkingAnimal('Jolene', 'llama', 'llama chow', 'midday')
gnash = WalkingAnimal('Gnash', 'cat', 'meow mix', 'afternoon')
rocco = WalkingAnimal('Rocco', 'cat', 'meow mix', 'afternoon')
pippi = WalkingAnimal('Pippi', 'cat', 'meow mix', 'morning')
fangor = WalkingAnimal('Fangor', 'cat', 'meow mix', 'morning')
echo = SwimmingAnimal('Echo', 'dolphin', 'fish')
willy = SwimmingAnimal('Willy', 'killer whale', 'fish')
jaws = SwimmingAnimal('Jaws', 'shark', 'fish')
ollie = SwimmingAnimal('Ollie', 'octopus', 'crab')
puffer = SwimmingAnimal('Puffer', 'puffer fish', 'fish food')
ellie = SwimmingAnimal('Ellie', 'eel', 'eel mix')
jericho = Snake('Jericho', 'morning', 'rat')
jake = Snake('Jake', 'midday', 'rat')
methusala = Snake('Methusala', 'afternoon', 'rat')
print(f'{bandit.name} the {bandit.species} is available to pet during the {bandit.shift} shift.')
print(jericho.feed())
print(jericho)


# Petting Zoo
varmint_village = PettingZoo("Varmint Village")
petting_zoo_animals = [bandit, jolene, gnash, rocco, pippi, fangor]
for animal in petting_zoo_animals:
    varmint_village.animals.append(animal)
print(f"{varmint_village.attraction_name} is where you'll find {varmint_village.description}, like")
for animal in varmint_village.animals:
    print(f"* {animal.name} the {animal.species.title()}")

slither_inn = SnakePit("Slither Inn")
snakes=[jericho, jake, methusala]
for snake in snakes:
    slither_inn.animals.append(snake)
print(f"{slither_inn.attraction_name} is where you'll find {slither_inn.description}, like")
for snake in slither_inn.animals:
    print(f"* {snake.name}")

poseidons_pets = Aquarium("Poseidon's Pets")
aquatic_animals = [echo, willy, jaws, ollie, puffer, ellie]
for animal in aquatic_animals:
    poseidons_pets.animals.append(animal)
print(f"{poseidons_pets.attraction_name} is where you'll find {poseidons_pets.description}, like")
for animal in poseidons_pets.animals:
    print(f"* {animal.name} the {animal.species.title()}")