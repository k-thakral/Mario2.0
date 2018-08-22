import os
import random
import signal
import time

from alarmexception import AlarmException
from board import board
from getch import _getChUnix as getChar
from globals import NUM_STONE_ROWS, NUM_COLS


class base():
    '''To get Basic ASCII representation of Character and get position'''
    str = []
    pos = []
    direction = ""

class mario():
    '''Class For Mario'''
    def __init__(self):
        self.str = []
        self.pos = []
        self.direction = ""
        self.str.append(['*'])
        self.str.append(['|'])
        self.direction = "right"
        self.pos.append(NUM_STONE_ROWS[0] - 2)
        self.legs_pos = NUM_STONE_ROWS[0] - 1
        self.pos.append(5)
    
    def draw(self, canvas, begin):
        for i in range(len(self.str)):
            for j in range(len(self.str[i])):
                canvas[self.pos[0] + i][begin[0] + self.pos[1] + j] = self.str[i][j]
    
    def move_mario(self, board, canvas, begin, enemy_list, score):
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
            quit()
        
        if c == 'd':
            os.system("tput reset")
            begin[0] += 1
            canvas[self.pos[0]][begin[0] + self.pos[1] - 1] = ' '
            canvas[self.pos[0] + 1][begin[0] + self.pos[1] - 1] = ' '
            self.direction = "right"
            for e in enemy_list:
                e.oscillate()
                e.draw(begin, canvas)
            board.draw(begin)
        
        if c == 'a':
            os.system("tput reset")
            begin[0] -= 1
            canvas[self.pos[0]][begin[0] + self.pos[1] + 1] = ' '
            canvas[self.pos[0] + 1][begin[0] + self.pos[1] + 1] = ' '
            self.direction = "left"
            for e in enemy_list:
                e.oscillate()
                e.draw(begin, canvas)
            board.draw(begin)
        
        if c == 'w':         
            if self.direction == "right":
                for i in range(5):
                    os.system("tput reset")
                    begin[0] += 1
                    self.pos[0] -= 1
                    canvas[self.pos[0] + 1][begin[0] + self.pos[1] - 1] = ' '
                    canvas[self.pos[0] + 2][begin[0] + self.pos[1] - 1] = ' '
                    canvas[self.pos[0]][begin[0] + self.pos[1]] = "*"
                    canvas[self.pos[0] + 1][begin[0] + self.pos[1]] = "|"
                    for e in enemy_list:
                        e.oscillate()
                        e.draw(begin, canvas)
                    board.draw(begin)
                    c = user_input()
                
                for i in range(5):
                    os.system("tput reset")
                    begin[0] += 1
                    self.pos[0] += 1
                    canvas[self.pos[0] - 1][begin[0] + self.pos[1] - 1] = ' '
                    canvas[self.pos[0]][begin[0] + self.pos[1] - 1] = ' '
                    canvas[self.pos[0]][begin[0] + self.pos[1]] = "*"
                    canvas[self.pos[0] + 1][begin[0] + self.pos[1]] = "|"
                    for e in enemy_list:
                        if self.legs_pos == e.pos_y and self.pos[1] + begin[0] == e.pos_x:
                            enemy_list.remove(e)
                            score[0] += 10
                        else:
                            e.draw(begin, canvas)
                            e.oscillate()
                    board.draw(begin)
                    c = user_input()
            
            if self.direction == "left":
                for i in range(5):
                    os.system("tput reset")
                    begin[0] -= 1
                    self.pos[0] -= 1
                    canvas[self.pos[0] + 1][begin[0] + self.pos[1] + 1] = ' '
                    canvas[self.pos[0] + 2][begin[0] + self.pos[1] + 1] = ' '
                    canvas[self.pos[0]][begin[0] + self.pos[1]] = "*"
                    canvas[self.pos[0] + 1][begin[0] + self.pos[1]] = "|"
                    for e in enemy_list:
                        if self.legs_pos == e.pos_y and self.pos[1] + begin[0] == e.pos_x:
                            enemy_list.remove(e)
                            score[0] += 10
                        else:
                            e.draw(begin, canvas)
                            e.oscillate()
                    board.draw(begin)
                    c = user_input()

                for i in range(5):
                    os.system("tput reset")
                    begin[0] -= 1
                    self.pos[0] += 1
                    canvas[self.pos[0] - 1][begin[0] + self.pos[1] + 1] = ' '
                    canvas[self.pos[0]][begin[0] + self.pos[1] + 1] = ' '
                    canvas[self.pos[0]][begin[0] + self.pos[1]] = "*"
                    canvas[self.pos[0] + 1][begin[0] + self.pos[1]] = "|"
                    for e in enemy_list:
                        if self.legs_pos == e.pos_y and self.pos[1] + begin[0] == e.pos_x:
                            enemy_list.remove(e)
                            score[0] += 10
                        else:
                            e.draw(begin, canvas)
                            e.oscillate()
                    board.draw(begin)
                    c = user_input()
                

class enemy():
    count = 0
    def __init__(self):
        self.str = []
        enemy.count += 1
        self.str.append(['E', 'E'])
        self.direction = "right"
        self.pos_x_start = random.randint(30, NUM_COLS - 20)
        self.pos_x = self.pos_x_start
        self.pos_x_end = self.pos_x_start + 10
        self.pos_y = NUM_STONE_ROWS[0] - 1
    
    def draw(self, begin, canvas):
        for i in range(len(self.str)):
            for j in range(len(self.str[i])):
                try:
                    if self.direction == "right":
                        canvas[self.pos_y + i][self.pos_x + j] = self.str[i][j]
                        canvas[self.pos_y + i][-2 + self.pos_x + j] = ' '
                    else:
                        canvas[self.pos_y + i][self.pos_x + j] = self.str[i][j]
                        canvas[self.pos_y + i][+2 + self.pos_x + j] = ' '
                except:
                    pass
    
    def oscillate(self):
        if self.direction == "right":
            if self.pos_x_end ==  self.pos_x:
                self.direction = "left"
            if self.pos_x < self.pos_x_end:
                self.pos_x += 1
        
        if self.direction == "left":
            if self.pos_x_start == self.pos_x:
                self.direction = "right"
            if self.pos_x > self.pos_x_start:
                self.pos_x -= 1
