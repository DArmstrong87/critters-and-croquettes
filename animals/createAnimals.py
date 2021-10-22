from datetime import date

class Animal:

    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.food = food
        self.__chip_number = chip_num
        self.date_added = date.today()

    @property
    def chip_number(self):
        return self.__chip_number

    @chip_number.setter
    def chip_number(self, number):
        pass

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class WalkingAnimal(Animal):

    def __init__(self, name, species, food, shift, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True

    def __str__(self):
        return f'{self.name} is a {self.species}'


class Snake(Animal):

    def __init__(self, name, species, food, shift, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.slithering = True

    def __str__(self):
        return f'{self.name} is a {self.species}'

    # Feed the snakes only weekly.
    def feed(self):
        if date.today().weekday() != 7:
            print(f"{self.name} is only to be fed once per week on Satrudays.")
        else:
            print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")} for its weekly feeding.')


class SwimmingAnimal(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

    def __str__(self):
        return f'{self.name} is a {self.species}'


class Llama(Animal):

    def __init__(self, name, species, food, shift, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True

    def __str__(self):
        return f'{self.name} is a {self.species}'

    def feed(self):
        print(f'{self.name} had "Rocky Top" sang to it as it was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')