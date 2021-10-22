from datetime import date

class Snake:

    def __init__(self, name, shift, food):
        self.name = name
        self.shift = shift
        self.species = 'Snake'
        self.food = food
        self.date_added = date.today()
        self.slithering = True

    def __str__(self):
        return f'{self.name} is a {self.species}'

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')