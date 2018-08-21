import os
import signal
import time

from alarmexception import AlarmException
from board import board
from getch import _getChUnix as getChar
from globals import NUM_STONE_ROWS


class base():
    '''To get Basic ASCII representation of Character and get position'''
    str = []
    pos = []
    direction = ""

class mario(base):
    '''Class For Mario'''
    def __init__(self):
        self.str.append(['*'])
        self.str.append(['|'])
        self.direction = "right"
        self.pos.append(NUM_STONE_ROWS[0] - 2)
        self.pos.append(5)
    
    def draw(self, canvas, begin):
        for i in range(len(self.str)):
            for j in range(len(self.str[i])):
                canvas[self.pos[0] + i][begin[0] + self.pos[1] + j] = self.str[i][j]
    
    def move_mario(self, board, canvas, begin):
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
            begin[0] += 1
            canvas[self.pos[0]][begin[0] + self.pos[1] - 1] = ' '
            canvas[self.pos[0] + 1][begin[0] + self.pos[1] - 1] = ' '
            self.direction = "right"
        
        if c == 'a':
            begin[0] -= 1
            canvas[self.pos[0]][begin[0] + self.pos[1] + 1] = ' '
            canvas[self.pos[0] + 1][begin[0] + self.pos[1] + 1] = ' '
            self.direction = "left"
        
        if c == 'w':         
            if self.direction == "right":
                for i in range(5):
                    os.system("tput reset")
                    begin[0] += 1
                    self.pos[0] -= 1
                    #self.pos[1] += 1
                    canvas[self.pos[0] + 1][begin[0] + self.pos[1] - 1] = ' '
                    canvas[self.pos[0] + 2][begin[0] + self.pos[1] - 1] = ' '
                    canvas[self.pos[0]][begin[0] + self.pos[1]] = "*"
                    canvas[self.pos[0] + 1][begin[0] + self.pos[1]] = "|"
                    board.draw(begin)
                    time.sleep(0.05)
                
                for i in range(5):
                    os.system("tput reset")
                    begin[0] += 1
                    self.pos[0] += 1
                    #self.pos[1] += 1
                    canvas[self.pos[0] - 1][begin[0] + self.pos[1] - 1] = ' '
                    canvas[self.pos[0]][begin[0] + self.pos[1] - 1] = ' '
                    canvas[self.pos[0]][begin[0] + self.pos[1]] = "*"
                    canvas[self.pos[0] + 1][begin[0] + self.pos[1]] = "|"
                    board.draw(begin)
                    time.sleep(0.05)
            
            if self.direction == "left":
                for i in range(5):
                    os.system("tput reset")
                    begin[0] -= 1
                    self.pos[0] -= 1
                    #self.pos[1] += 1
                    canvas[self.pos[0] + 1][begin[0] + self.pos[1] + 1] = ' '
                    canvas[self.pos[0] + 2][begin[0] + self.pos[1] + 1] = ' '
                    canvas[self.pos[0]][begin[0] + self.pos[1]] = "*"
                    canvas[self.pos[0] + 1][begin[0] + self.pos[1]] = "|"
                    board.draw(begin)
                    time.sleep(0.05)

                for i in range(5):
                    os.system("tput reset")
                    begin[0] -= 1
                    self.pos[0] += 1
                    #self.pos[1] += 1
                    canvas[self.pos[0] - 1][begin[0] + self.pos[1] + 1] = ' '
                    canvas[self.pos[0]][begin[0] + self.pos[1] + 1] = ' '
                    canvas[self.pos[0]][begin[0] + self.pos[1]] = "*"
                    canvas[self.pos[0] + 1][begin[0] + self.pos[1]] = "|"
                    board.draw(begin)
                    time.sleep(0.05)
                

