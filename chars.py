import os
import random
import signal
import time

from alarmexception import AlarmException
from board import board
from getch import _getChUnix as getChar
from globals import NUM_COLS, NUM_STONE_ROWS


class base():
    '''To get Basic ASCII representation of Character and get position'''

    def __init__(self):
        self._str = []
        self.pos = []
        self.direction = ""


class mario(base):
    '''Class For Mario'''

    def __init__(self):
        self._str = []
        self.pos = []
        self.direction = ""
        self._str.append(['*'])
        self._str.append(['|'])
        self.direction = "right"
        self.pos.append(NUM_STONE_ROWS[0] - 2)
        self.legs_pos = NUM_STONE_ROWS[0] - 1
        self.pos.append(5)

    def draw(self, canvas, begin, base_level):
        for i in range(len(self._str)):
            for j in range(len(self._str[i])):
                canvas[base_level + self.pos[0] + i][begin[0] +
                                                     self.pos[1] + j] = self._str[i][j]

    def move_mario(self, board, canvas, begin, enemy_list, score,
                   base_level, base_level_next, base_level_prev):
        """Moves Mario"""
        def alarmhandler(signum, frame):
            ''' input method '''
            raise AlarmException

        def user_input(timeout=0.1):
            ''' input method '''
            signal.signal(signal.SIGALRM, alarmhandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            try:
                text = getChar()()
                signal.alarm(0)
                return text
            except AlarmException:
                pass
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return ''

        c = user_input()

        if c == 'q':
            os.system("fuser -k -TERM ./theme.mp3")
            quit()

        if c == 'd':
            os.system("tput reset")
            if base_level_next >= base_level:
                begin[0] += 1
                canvas[base_level + self.pos[0]
                       ][begin[0] + self.pos[1] - 1] = ' '
                canvas[base_level + self.pos[0] +
                       1][begin[0] + self.pos[1] - 1] = ' '
                self.direction = "right"
            for e in enemy_list:
                e.oscillate()
                e.draw(begin, canvas)
            board.draw(begin)

        if c == 'a':
            os.system("tput reset")
            if base_level_prev >= base_level:
                begin[0] -= 1
                canvas[base_level + self.pos[0]
                       ][begin[0] + self.pos[1] + 1] = ' '
                canvas[base_level + self.pos[0] +
                       1][begin[0] + self.pos[1] + 1] = ' '
                self.direction = "left"
            for e in enemy_list:
                e.oscillate()
                e.draw(begin, canvas)
            board.draw(begin)

        if c == 'w':
            if self.direction == "right":
                os.system("cvlc --play-and-exit ./jump.mp3 &")
                for i in range(5 - base_level):
                    os.system("tput reset")
                    begin[0] += 1
                    self.pos[0] -= 1
                    canvas[base_level + self.pos[0] +
                           1][begin[0] + self.pos[1] - 1] = ' '
                    canvas[base_level + self.pos[0] +
                           2][begin[0] + self.pos[1] - 1] = ' '
                    canvas[base_level + self.pos[0]
                           ][begin[0] + self.pos[1]] = "*"
                    canvas[base_level + self.pos[0] +
                           1][begin[0] + self.pos[1]] = "|"
                    for e in enemy_list:
                        e.oscillate()
                        e.draw(begin, canvas)
                    board.draw(begin)
                    c = user_input()

                for i in range(5 - base_level):
                    os.system("tput reset")
                    begin[0] += 1
                    self.pos[0] += 1
                    canvas[base_level + self.pos[0] -
                           1][begin[0] + self.pos[1] - 1] = ' '
                    canvas[base_level + self.pos[0]
                           ][begin[0] + self.pos[1] - 1] = ' '
                    canvas[base_level + self.pos[0]
                           ][begin[0] + self.pos[1]] = "*"
                    canvas[base_level + self.pos[0] +
                           1][begin[0] + self.pos[1]] = "|"
                    for e in enemy_list:
                        if self.legs_pos == e.pos_y and self.pos[1] + \
                                begin[0] == e.pos_x:
                            enemy_list.remove(e)
                            score[0] += 10
                        else:
                            e.draw(begin, canvas)
                            e.oscillate()
                    board.draw(begin)
                    c = user_input()

            if self.direction == "left":
                os.system("cvlc --play-and-exit ./jump.mp3 &")
                for i in range(5 - base_level):

                    os.system("tput reset")
                    begin[0] -= 1
                    self.pos[0] -= 1
                    canvas[base_level + self.pos[0] + 1][base_level +
                                                         begin[0] + self.pos[1] + 1] = ' '
                    canvas[base_level + self.pos[0] +
                           2][begin[0] + self.pos[1] + 1] = ' '
                    canvas[base_level + self.pos[0]
                           ][begin[0] + self.pos[1]] = "*"
                    canvas[base_level + self.pos[0] +
                           1][begin[0] + self.pos[1]] = "|"
                    for e in enemy_list:
                        if self.legs_pos == e.pos_y and self.pos[1] + \
                                begin[0] == e.pos_x:
                            enemy_list.remove(e)
                            score[0] += 10
                        else:
                            e.draw(begin, canvas)
                            e.oscillate()
                    board.draw(begin)
                    c = user_input()

                for i in range(5 - base_level):
                    os.system("tput reset")
                    begin[0] -= 1
                    self.pos[0] += 1
                    canvas[base_level + self.pos[0] -
                           1][begin[0] + self.pos[1] + 1] = ' '
                    canvas[base_level + self.pos[0]
                           ][begin[0] + self.pos[1] + 1] = ' '
                    canvas[base_level + self.pos[0]
                           ][begin[0] + self.pos[1]] = "*"
                    canvas[base_level + self.pos[0] +
                           1][begin[0] + self.pos[1]] = "|"
                    for e in enemy_list:
                        if self.legs_pos == e.pos_y and self.pos[1] + \
                                begin[0] == e.pos_x:
                            enemy_list.remove(e)
                            score[0] += 10
                        else:
                            e.draw(begin, canvas)
                            e.oscillate()
                    board.draw(begin)
                    c = user_input()


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
