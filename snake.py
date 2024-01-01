import random

class Snake:
    def __init__(self):
        self.color = "green"
        self.width = 15
        self.height = 15
        self.pos_x = 200
        self.pos_y = 200
        self.snake_length = 1
        self.movement_rate = 5
    
    def move_right(self):
        self.pos_x += self.movement_rate

    def move_left(self):
        self.pos_x -= self.movement_rate

    def move_up(self):
        self.pos_y -= self.movement_rate

    def move_down(self):
        self.pos_y += self.movement_rate
    
    def grow_length(self):
        self.snake_length += 1

