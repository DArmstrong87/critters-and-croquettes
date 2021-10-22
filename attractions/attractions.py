class PettingZoo:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()

    @property
    def last_critter_added(self):
        return self.animals[-1]

class SnakePit:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "a stupendous, slithering snake sanctuary with many snakes"
        self.animals = list()

    @property
    def last_critter_added(self):
        return self.animals[-1]

class Aquarium:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "all the amazing creatures under the sea"
        self.animals = list()

    @property
    def last_critter_added(self):
        return self.animals[-1]
