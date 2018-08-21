import random
from globals import NUM_STONE_ROWS, NUM_COLS

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

class pit():
    
    def __init__(self):
        self.start = random.randint(20, NUM_COLS-20)
        self.end = random.randint(self.start, self.start + 7)
    
    def draw(self, canvas):
        for i in range(self.start, self.end):
            for j in range(NUM_STONE_ROWS[0], NUM_STONE_ROWS[1]):
                canvas[j][i] = ' '

    def check_fall(self, mario, begin):
        if mario.pos[1] + begin[0] > self.start and mario.pos[1] + begin[0] < self.end:
            return False
        else:
            return True        
                
class obstacle():
    def __init__(self):
        self.str = [
            [' ', '_', '_', '_', '_', '_', ' ',],
            ['[', ' ', ' ', ' ', ' ', ' ', ']',],
        ]

        self.pos_x = NUM_STONE_ROWS[0] - random.randint(0, 3) - 1

        for i in range(NUM_STONE_ROWS[0] - self.pos_x - 1):
            self.str.append(
                [' ', '|', ' ', ' ', ' ', '|', ' ']
            )
        
        self.pos_y = random.randint(20, NUM_COLS - 20)

    def __str__(self):
        return str(self.pos_x) + " " + str(self.pos_y)

    def draw(self, canvas, begin):
        for i in range(len(self.str)):
            for j in range(len(self.str[i])):
                canvas[self.pos_x + i][self.pos_y + j] = self.str[i][j]
    
    def check(self, mario, begin):
        if mario.pos[0] + 1 < self.pos_x and begin[0] + mario.pos[1] > self.pos_y and begin[0] + mario.pos[1] < self.pos_y + 6:
            return False
        else:
            return True
