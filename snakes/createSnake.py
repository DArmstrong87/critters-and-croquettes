from datetime import date

class Snake:

    def __init__(self, name):
        self.name = name
        self.species = 'Snake'
        self.date_added = date.today()
        self.slithering = True