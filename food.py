import random

class Food:

    def __init__(self):
        self.pos_x = random.randrange(1, 1280)
        self.pos_y = random.randrange(1, 720)
        self.width = 12
        self.height = 12
        self.color = "yellow"