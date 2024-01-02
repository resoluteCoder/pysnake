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

    def has_eaten(self, pos_x, pos_y, height, width):
        has_collided_x = self.pos_x >= pos_x - (width / 2) and self.pos_x <= pos_x + (width / 2)
        has_collided_y = self.pos_y <= pos_y + (height / 2) and self.pos_y >= pos_y - (height / 2)

        return has_collided_x and has_collided_y