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
base_level = NUM_STONE_ROWS[0] - 1
enemy_list = []
enem_flag= False
SCORE = [0]

for i in range(20):
    c = cloud()

    if cloud_list == []:
        cloud_list.append(c)
        c.draw(BOARD.canvas, begin)
    else:
        for clouds in cloud_list:
            if abs(c.pos_y - clouds.pos_y) > 10:
                if len(cloud_list) <= 20:
                    cloud_list.append(c)

pit_start_list = [20, 40, 78, 103, 144, 169, 196, 225]
pit_end_list = [25, 46, 82, 109, 147, 175, 201, 231]

for i in range(len(pit_start_list)):
    p = pit()
    p.start = pit_start_list[i]
    p.end = pit_end_list[i]
    pit_list.append(p)

enemy_path_list = [(26, 35), (53, 69), (90, 96), (148, 160), (203, 212)]

obstacle_presence_list = [47, 83, 112, 131, 183, 215] 

for i in range(len(enemy_path_list)):
    e = enemy()
    e.pos_x_start = enemy_path_list[i][0]
    e.pos_x_end = enemy_path_list[i][1]
    e.pos_x = e.pos_x_start
    enemy_list.append(e)

for i in range(len(obstacle_presence_list)):
    o = obstacle()
    o.pos_y = obstacle_presence_list[i]
    obstacle_list.append(o)

while True:
    os.system("tput reset")
    MARIO.draw(BOARD.canvas, begin)
    print(SCORE[0])

    for c in cloud_list:
        c.draw(BOARD.canvas, begin)
    
    for p in pit_list:
        p.draw(BOARD.canvas)
    
    for p in pit_list:
        if p.check_fall(MARIO, begin) is False:
            quit()
    
    for o in obstacle_list:
        print(o.pos_y)
        o.draw(BOARD.canvas, begin)
    
    for e in enemy_list:
        e.draw(begin, BOARD.canvas)
        e.oscillate()
        if e.pos_x == begin[0] + MARIO.pos[1] and MARIO.pos[1] == e.pos_y:
            quit()
        elif e.pos_x == begin[0] + MARIO.pos[1] and MARIO.legs_pos == e.pos_y:
            enemy_list.remove(e)
            SCORE[0] += 10
    
    BOARD.draw(begin)
    MARIO.move_mario(BOARD, BOARD.canvas, begin, enemy_list, SCORE)
