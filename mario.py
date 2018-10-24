'''Classes for Mario'''
import os
import signal

from alarmexception import AlarmException
from getch import _getChUnix as getChar
from globals import NUM_STONE_ROWS


class Mario():
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
        '''Draw Mario on the canvas'''
        for i in range(len(self._str)):
            for j in range(len(self._str[i])):
                canvas[base_level + self.pos[0] + i][begin[0] + \
                    self.pos[1] + j] = self._str[i][j]

    def move_mario(
            self,
            board,
            canvas,
            begin,
            enemy_list,
            score,
            base_level,
            base_level_next,
            base_level_prev,
            boss,
            coin_list):
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

        char = user_input()

        if char == 'q':
            os.system("fuser -k -TERM ./theme.wav")
            quit()

        if char == 'd':
            os.system("tput reset")
            if base_level_next >= base_level:
                begin[0] += 1
                canvas[base_level + self.pos[0]][begin[0] + self.pos[1] - 1] = ' '
                canvas[base_level + self.pos[0] +1][begin[0] + self.pos[1] - 1] = ' '
                self.direction = "right"
            boss.oscillate()
            for e in enemy_list:
                e.oscillate()
                e.draw(canvas)
            boss.draw(canvas)
            board.draw(begin)

        if char == 'a':
            os.system("tput reset")
            if base_level_prev >= base_level:
                begin[0] -= 1
                canvas[base_level + self.pos[0]][begin[0] + self.pos[1] + 1] = ' '
                canvas[base_level + self.pos[0] +1][begin[0] + self.pos[1] + 1] = ' '
                self.direction = "left"
            for e in enemy_list:
                e.oscillate()
                e.draw(canvas)
            boss.check(mario=self, begin=begin, score=score)
            boss.oscillate()
            boss.draw(canvas)
            board.draw(begin)

        if char == 'w':
            if self.direction == "right":
                os.system("aplay ./jump.wav &")
                for i in range(5 - base_level):
                    i += 1
                    i -= 1
                    os.system("tput reset")
                    begin[0] += 1
                    self.pos[0] -= 1
                    canvas[base_level + self.pos[0] +1][begin[0] + self.pos[1] - 1] = ' '
                    canvas[base_level + self.pos[0] +2][begin[0] + self.pos[1] - 1] = ' '
                    canvas[base_level + self.pos[0]][begin[0] + self.pos[1]] = "*"
                    canvas[base_level + self.pos[0] +1][begin[0] + self.pos[1]] = "|"

                    for enemy in enemy_list:
                        enemy.oscillate()
                        enemy.draw(canvas)
                    for c in coin_list:
                        if c.check(mario=self, begin=begin):
                            coin_list.remove(c)
                            score[0] += 1
                    boss.check(mario=self, begin=begin, score=score)
                    boss.oscillate()
                    boss.draw(canvas)
                    board.draw(begin)
                    char = user_input()

                for i in range(5 - base_level):
                    os.system("tput reset")
                    begin[0] += 1
                    self.pos[0] += 1
                    canvas[base_level + self.pos[0] -1][begin[0] + self.pos[1] - 1] = ' '
                    canvas[base_level + self.pos[0]][begin[0] + self.pos[1] - 1] = ' '
                    canvas[base_level + self.pos[0]][begin[0] + self.pos[1]] = "*"
                    canvas[base_level + self.pos[0] +1][begin[0] + self.pos[1]] = "|"
                    for e in enemy_list:
                        if self.legs_pos == e.pos_y and self.pos[1] + \
                                begin[0] == e.pos_x:
                            enemy_list.remove(e)
                            score[0] += 10
                        else:
                            e.draw(canvas)
                            e.oscillate()
                    for c in coin_list:
                        if c.check(mario=self, begin=begin):
                            coin_list.remove(c)
                            score[0] += 1
                    boss.check(mario=self, begin=begin, score=score)
                    boss.oscillate()
                    boss.draw(canvas)
                    board.draw(begin)
                    char = user_input()

            if self.direction == "left":
                os.system("aplay ./jump.wav &")
                for i in range(5 - base_level):

                    os.system("tput reset")
                    begin[0] -= 1
                    self.pos[0] -= 1
                    canvas[base_level + self.pos[0] + 1][base_level + begin[0] + self.pos[1] + 1] = ' '
                    canvas[base_level + self.pos[0] +2][begin[0] + self.pos[1] + 1] = ' '
                    canvas[base_level + self.pos[0]][begin[0] + self.pos[1]] = "*"
                    canvas[base_level + self.pos[0] + 1][begin[0] + self.pos[1]] = "|"
                    for e in enemy_list:
                        if self.legs_pos == e.pos_y and self.pos[1] + \
                                begin[0] == e.pos_x:
                            enemy_list.remove(e)
                            score[0] += 10
                        else:
                            e.draw(canvas)
                            e.oscillate()
                    for c in coin_list:
                        if c.check(mario=self, begin=begin):
                            coin_list.remove(c)
                            score[0] += 1
                    boss.check(mario=self, begin=begin, score=score)
                    boss.oscillate()
                    boss.draw(canvas)
                    board.draw(begin)
                    char = user_input()

                for i in range(5 - base_level):
                    os.system("tput reset")
                    begin[0] -= 1
                    self.pos[0] += 1
                    canvas[base_level + self.pos[0] -
                           1][begin[0] + self.pos[1] + 1] = ' '
                    canvas[base_level + self.pos[0]][begin[0] + self.pos[1] + 1] = ' '
                    canvas[base_level + self.pos[0]][begin[0] + self.pos[1]] = "*"
                    canvas[base_level + self.pos[0] + 1][begin[0] + self.pos[1]] = "|"
                    for e in enemy_list:
                        if self.legs_pos == e.pos_y and self.pos[1] + \
                                begin[0] == e.pos_x:
                            enemy_list.remove(e)
                            score[0] += 10
                        else:
                            e.draw(canvas)
                            e.oscillate()
                    for c in coin_list:
                        if c.check(mario=self, begin=begin):
                            coin_list.remove(c)
                            score[0] += 1
                    boss.check(mario=self, begin=begin, score=score)
                    boss.oscillate()
                    boss.draw(canvas)
                    board.draw(begin)
                    char = user_input()
