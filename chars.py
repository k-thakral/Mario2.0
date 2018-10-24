'''Make the Boss and the Enemies'''
import random
from globals import NUM_COLS, NUM_STONE_ROWS


class Enemy():
    '''To make Basic Enemies'''
    count = 0

    def __init__(self):
        '''Make the String for the Enemy'''
        self._str = []
        Enemy.count += 1
        self._str.append(['E', 'E'])
        self.direction = "right"
        self.pos_x_start = random.randint(30, NUM_COLS - 20)
        self.pos_x = self.pos_x_start
        self.pos_x_end = self.pos_x_start + 10
        self.pos_y = NUM_STONE_ROWS[0] - 1

    def draw(self, canvas):
        '''Draw the enemy on the canvas'''
        for i in range(len(self._str)):
            for j in range(len(self._str[i])):
                try:
                    if self.direction == "right":
                        canvas[self.pos_y + i][self.pos_x + j] = self._str[i][j]
                        canvas[self.pos_y + i][-2 + self.pos_x + j] = ' '
                    else:
                        canvas[self.pos_y + i][self.pos_x + j] = self._str[i][j]
                        canvas[self.pos_y + i][+2 + self.pos_x + j] = ' '
                except BaseException:
                    pass

    def oscillate(self):
        '''Move the Enemy'''
        if self.direction == "right":
            if self.pos_x_end == self.pos_x:
                self.direction = "left"
            if self.pos_x < self.pos_x_end:
                self.pos_x += 1

        if self.direction == "left":
            if self.pos_x_start == self.pos_x:
                self.direction = "right"
            if self.pos_x > self.pos_x_start:
                self.pos_x -= 1


class Boss():
    '''Make The Boss'''
    def __init__(self):
        '''Draw the string of the Boss'''
        self._life = 3
        self._str = [
            [' ', ' ', str(self._life), str(self._life), ' ', ' '],
            [' ', 'B', 'B', 'B', 'B', ' ']
        ]

        self.pos_x_start = NUM_COLS - 40
        self.pos_x_end = NUM_COLS - 20
        self.pos_x = self.pos_x_start
        self.pos_y = NUM_STONE_ROWS[0] - 2
        self.direction = "right"

    def draw(self, canvas):
        '''Draw boss on the canvas'''
        for i in range(len(self._str)):
            for j in range(len(self._str[i])):
                canvas[self.pos_y + i][self.pos_x + j] = self._str[i][j]

    def oscillate(self):
        '''Move the Boss'''
        if self.direction == "right":
            if self.pos_x_end == self.pos_x:
                self.direction = "left"
            if self.pos_x < self.pos_x_end:
                self.pos_x += 1

        if self.direction == "left":
            if self.pos_x_start == self.pos_x:
                self.direction = "right"
            if self.pos_x > self.pos_x_start:
                self.pos_x -= 1

    def check(self, mario, begin, score):
        '''Check collision between mario and Boss'''
        if mario.pos[1] + begin[0] in range(self.pos_x,
                                            self.pos_x + 5) and mario.pos[0] == self.pos_y - 2:
            self._life -= 1
            self._str = [
                [' ', ' ', str(self._life), str(self._life), ' ', ' '],
                [' ', 'B', 'B', 'B', 'B', ' ']
            ]
            score[0] += 50

    def check_life(self):
        '''Check if Boss is dead'''
        if self._life <= 0:
            return False
        return True
