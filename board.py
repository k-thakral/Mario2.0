from globals import *

class board():
    '''This class is to create the canvas'''
    canvas = [ [] for i in range(NUM_ROWS) ]

    def __init__(self):
        for i in range(0, NUM_ROWS):
            for j in range(NUM_COLS):
                self.canvas[i].append(' ')
        
        for j in range(NUM_COLS):
            self.canvas[NUM_STONE_ROWS[0]][j] = '_'

        for i in range(NUM_STONE_ROWS[0] + 1, NUM_STONE_ROWS[1]):
            for j in range(0,NUM_COLS,4):
                #print(len(self.canvas))
                #print(i, j)
                self.canvas[i][j] = '|'
                self.canvas[i][j + 1] = '_'
                self.canvas[i][j + 2] = '_'
                self.canvas[i][j + 3] = '|'
    

    def draw(self, begin):
        for i in self.canvas:
            temp = ''
            for j in i[begin[0]:begin[0]+80]:
                temp += j
            print(temp)
