import os
from colorama import init, Fore, Back
from board import board
from chars import enemy, mario, boss
from globals import NUM_STONE_ROWS, NUM_COLS
from scenery import cloud, obstacle, pit, coins

init()

def GameLoop(LIVES = 2, SCORE = [0]):
    BOARD = board()
    MARIO = mario()
    begin = [0]
    cloud_list = []
    pit_list = []
    obstacle_list = []
    base_level = [0 for i in range(NUM_COLS)]
    coin_list = []
    enemy_list = []
    SCORE = [0]
    BOSS = boss()

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

    while len(coin_list) != 50:
        c = coins()
        flag = True 
        for p in pit_presence_list:
            if c.pos_x >= p[0] and c.pos_x <= p[1]:
                flag = False
        
        if flag == True:
            coin_list.append(c)
                

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

    os.system("cvlc --play-and-exit ./theme.mp3 &")
    while True:
        os.system("tput reset")
        BOSS.oscillate()
        BOSS.draw(BOARD.canvas)

        MARIO.draw(BOARD.canvas, begin, base_level[MARIO.pos[1] + begin[0]])
        print("Score : " + str(SCORE[0]) + "\tLives : " + str(LIVES))

        for c in cloud_list:
            c.draw(BOARD.canvas, begin)

        for p in pit_list:
            p.draw(BOARD.canvas)
        
        for c in coin_list:
            if c.check(MARIO, begin=begin):
                coin_list.remove(c)
                SCORE[0] += 1
                continue
            else:
                c.draw(BOARD.canvas, begin)

        for p in pit_list:
            if p.check_fall(MARIO, begin) is False:
                os.system("fuser -k -TERM ./theme.mp3")
                start_screen()

        for o in obstacle_list:
            # print(o.pos_y)
            o.draw(BOARD.canvas, begin)

        for e in enemy_list:
            e.draw(begin, BOARD.canvas)
            e.oscillate()
            if e.pos_x == begin[0] + MARIO.pos[1] and MARIO.legs_pos == e.pos_y:
                os.system("fuser -k -TERM ./theme.mp3")
                LIVES -= 1
                SCORE[0] += 10
                enemy_list.remove(e)
                if LIVES == 0:
                    start_screen()
                else:
                    break
                #quit()
            elif e.pos_x == begin[0] + MARIO.pos[1] and MARIO.legs_pos + 1 == e.pos_y:
                enemy_list.remove(e)
                SCORE[0] += 10
        
        if BOSS.check_life() == False:
            Game_End(SCORE)

        BOARD.draw(begin)
        MARIO.move_mario(BOARD, BOARD.canvas, begin, enemy_list, SCORE,
                         base_level[MARIO.pos[1] + begin[0]], base_level[MARIO.pos[1] + begin[0] + 1], base_level[MARIO.pos[1] + begin[0] - 1], BOSS,coin_list=coin_list)

def start_screen():
    os.system('tput reset')
    print("\t\t\t\t\t\t\t\t" + Fore.RED + Back.BLUE + "Hello, Welcome To Mario2.0 !" + Back.BLACK)
    print(Fore.GREEN + Back.BLACK + "Press P to play")
    print(Fore.GREEN + Back.BLACK + "Press Q to quit")
    x = input()

    if x == 'p' or x == 'P':
        GameLoop()
    else:
        quit()

def Game_End(score):
    os.system('tput reset')
    print("\t\t\t\t\t\t\t\t" + Fore.RED + Back.BLUE +
          "Thanks For Playing Mario2.0 !" + Back.BLACK)
    print("\t\t\t\t\t\t\t\t" + Fore.RED + Back.BLUE +
          "Your Final Score is " + str(score[0]) + Back.BLACK)
    print(Fore.GREEN + Back.BLACK + "Press P to play")
    print(Fore.GREEN + Back.BLACK + "Press Q to quit")
    
    x = input()
    if x == 'p' or 'P':
        GameLoop()
    else:
        quit()

start_screen()
