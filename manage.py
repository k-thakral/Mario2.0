import os

from board import board
from chars import enemy, mario
from globals import NUM_STONE_ROWS, NUM_COLS
from scenery import cloud, obstacle, pit


BOARD = board()
MARIO = mario()
begin = [0]
cloud_list = []
pit_list = []
obstacle_list = []
base_level = [0 for i in range(NUM_COLS)]
enemy_list = []
enem_flag = False
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

pit_presence_list = [(20, 25), (40, 46), (78, 82), (103, 109),
                     (144, 147), (169, 175), (196, 201), (225, 231)]

for i in range(len(pit_presence_list)):
    p = pit()
    p.start = pit_presence_list[i][0]
    p.end = pit_presence_list[i][1]
    pit_list.append(p)

enemy_path_list = [(26, 35), (53, 69), (90, 96), (148, 160), (203, 212)]

obstacle_presence_list = [
    (47, 53), (83, 89), (112, 118), (131, 137), (183, 189), (215, 221)]


for i in range(len(enemy_path_list)):
    e = enemy()
    e.pos_x_start = enemy_path_list[i][0]
    e.pos_x_end = enemy_path_list[i][1]
    e.pos_x = e.pos_x_start
    enemy_list.append(e)

for i in range(len(obstacle_presence_list)):
    o = obstacle()
    o.pos_y = obstacle_presence_list[i][0]
    obstacle_list.append(o)

for i in range(NUM_COLS):
    flag = 1
    for o in obstacle_list:
        if i >= o.pos_y and i <= o.pos_y + 6:
            flag = 0
            base_level[i] = -1 * (NUM_STONE_ROWS[0] - o.pos_x)
    if flag == 0:
        continue
