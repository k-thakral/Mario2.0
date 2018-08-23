import os
import random
import signal
import time

from alarmexception import AlarmException
from board import board
from getch import _getChUnix as getChar
from globals import NUM_COLS, NUM_STONE_ROWS
from base_chars import base

class enemy(base):
    count = 0

    def __init__(self):
        self._str = []
        enemy.count += 1
        self._str.append(['E', 'E'])
        self.direction = "right"
        self.pos_x_start = random.randint(30, NUM_COLS - 20)
        self.pos_x = self.pos_x_start
        self.pos_x_end = self.pos_x_start + 10
        self.pos_y = NUM_STONE_ROWS[0] - 1

    def draw(self, begin, canvas):
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


class boss():
    def __init__(self):
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
        for i in range(len(self._str)):
            for j in range(len(self._str[i])):
                canvas[self.pos_y + i][self.pos_x + j] = self._str[i][j]

    def oscillate(self):
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
        if mario.pos[1] + begin[0] in range(self.pos_x,
                                            self.pos_x + 5) and mario.pos[0] == self.pos_y - 2:
            self._life -= 1
            self._str = [
                [' ', ' ', str(self._life), str(self._life), ' ', ' '],
                [' ', 'B', 'B', 'B', 'B', ' ']
            ]
            score[0] += 50

    def check_life(self):
        if self._life <= 0:
            return False
        else:
            return True
