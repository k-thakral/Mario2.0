import os

from board import board
from chars import mario
from scenery import cloud

BOARD = board()
MARIO = mario()
begin = [0]
cloud_list = []

while True:
    os.system('tput reset')
    MARIO.draw(BOARD.canvas, begin)
    #print(cloud_list)
    x = cloud()
    #print(x.pos_x, x.pos_y)
    if cloud_list != []:
        for clouds in cloud_list:
            if (x.pos_y - clouds.pos_y) > 10:
                if len(cloud_list) <= 20:
                    x.draw(BOARD.canvas, begin)
                    cloud_list.append(x)
    else:
        cloud_list.append(x)
        x.draw(BOARD.canvas, begin)
        #print(cloud_list)

    BOARD.draw(begin)
    MARIO.move_mario(BOARD, BOARD.canvas, begin)
