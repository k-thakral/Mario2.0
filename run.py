import os

from board import board
from chars import mario, enemy
from scenery import cloud, obstacle, pit
from globals import NUM_STONE_ROWS

BOARD = board()
MARIO = mario()
begin = [0]
cloud_list = []
pit_list = []
obstacle_list = []
base_level = NUM_STONE_ROWS[0]
enemy_list = []

while True:
    os.system('tput reset')
    MARIO.draw(BOARD.canvas, begin)

    x = cloud()

    if cloud_list != []:
        for clouds in cloud_list:
            if abs(x.pos_y - clouds.pos_y) > 10:
                if len(cloud_list) <= 20:
                    x.draw(BOARD.canvas, begin)
                    cloud_list.append(x)
    else:
        cloud_list.append(x)
        x.draw(BOARD.canvas, begin)
    
    y = pit()

    if pit_list != []:
        for p in pit_list:
            if abs(p.start - y.start) > 10:
                if len(pit_list) <= 10:
                    y.draw(BOARD.canvas)
                    pit_list.append(y)
    else:
        pit_list.append(y)
        y.draw(BOARD.canvas)
    
    for p in pit_list:
        if p.check_fall(MARIO, begin) is False:
            quit()
    
    #z = obstacle()
    #
    #if obstacle_list != []:
    #    for o in obstacle_list:
    #        for p in pit_list:
    #            if abs(o.pos_x - z.pos_x) > 10 or abs(p.start - z.pos_x) > 10:
    #                if len(obstacle_list) <= 10:
    #                    z.draw(BOARD.canvas, begin)
    #                    obstacle_list.append(z)
    #else:
    #    obstacle_list.append(z)
    #    z.draw(BOARD.canvas, begin)
    if len(enemy_list) <= 5:
        for i in range(5):
            e = enemy()
            for p in pit_list:
                if p.start > e.pos_x_start and e.pos_x_end > p.end:
                    e.pos_x_start = p.start + 1
                    e.pos_x_end = p.end - 1
                elif p.start < e.pos_x_start and e.pos_x_end > p.end:
                    e.pos_x_start = p.end + 1
                elif p.start > e.pos_x_start and e.pos_x_end < p.end:
                    e.pos_x_end = p.start - 1
                elif p.start < e.pos_x_start and e.pos_x_end < p.end:
                    continue
                if len(enemy_list) <= 5:
                    if enemy_list != []:
                        for z in enemy_list:
                            if abs(z.pos_x_start - e.pos_x_start) > 30:    
                                enemy_list.append(e)
                    else:
                        enemy_list.append(e)
    for e in enemy_list:
        e.oscillate()
        if e.pos_x < begin[0]:
            del e
        else:
            e.draw(begin, BOARD.canvas)
        #print(e.pos_x_start, e.pos_x_end)

    BOARD.draw(begin)
    MARIO.move_mario(BOARD, BOARD.canvas, begin, enemy_list)
