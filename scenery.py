import random
from globals import *

class cloud():

    def __init__(self):
        self.str = [
            [' ', ' ', ' ', '_', '_', ' ', ' ', ' '],
            [' ', '_', '(', ' ', ' ', ')', '_', ' '],
            ['(', '_', '_', '_', '_', '_', '_', ')']
        ]

        self.pos_x = random.randint(0, 15)
        self.pos_y = random.randint(0, NUM_COLS - 20)
    
    def draw(self, canvas, begin):
        for i in range(len(self.str)):
            for j in range(len(self.str[i])):
                canvas[self.pos_x + i][self.pos_y + j] = self.str[i][j]
    
    def __str__(self):
        return str(self.pos_x) + ',' + str(self.pos_y)
                
