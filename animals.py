# import the python datetime module to help us create a timestamp
from animals import Snake, SwimmingAnimal, WalkingAnimal, Llama
from attractions import PettingZoo, SnakePit, Aquarium

bandit = WalkingAnimal('Bandit', 'raccoon', 'raccoon chow', 'morning', 1111)

jolene = Llama('Jolene', 'llama', 'llama chow', 'midday', 2222)
gnash = WalkingAnimal('Gnash', 'cat', 'meow mix', 'afternoon', 3333)
rocco = WalkingAnimal('Rocco', 'cat', 'meow mix', 'afternoon', 4444)
pippi = WalkingAnimal('Pippi', 'cat', 'meow mix', 'morning', 5555)
fangor = WalkingAnimal('Fangor', 'cat', 'meow mix', 'morning', 6666)
print(f'{bandit.name} the {bandit.species} is available to pet during the {bandit.shift} shift.')
print(bandit.feed())
print(jolene.feed())

echo = SwimmingAnimal('Echo', 'dolphin', 'fish', 5126)
willy = SwimmingAnimal('Willy', 'killer whale', 'fish', 3456)
jaws = SwimmingAnimal('Jaws', 'shark', 'fish', 3264)
ollie = SwimmingAnimal('Ollie', 'octopus', 'crab', 83127)
puffer = SwimmingAnimal('Puffer', 'puffer fish', 'fish food', 7125)
ellie = SwimmingAnimal('Ellie', 'eel', 'eel mix', 6424)


jericho = Snake('Jericho', 'Boa', 'rat', 'morning', 7146)
jake = Snake('Jake', 'Python', 'rat', 'midday', 1125)
methusala = Snake('Methusala',  'Anaconda', 'rat', 'afternoon', 2796)
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
snakes = [jericho, jake, methusala]
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
