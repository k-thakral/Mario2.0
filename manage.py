'''Run the Game'''
import os
from colorama import init, Fore, Back
from board import Board
from chars import Enemy, Boss
from mario import Mario
from globals import NUM_STONE_ROWS, NUM_COLS
from scenery import Cloud, Obstacle, Pit, Coins

init()


def game_loop(lives=3, score=[0]):
    '''Run The Game'''
    board = Board()
    mario = Mario()
    begin = [0]
    cloud_list = []
    pit_list = []
    obstacle_list = []
    base_level = [0 for i in range(NUM_COLS)]
    coin_list = []
    enemy_list = []
    score = [0]
    boss = Boss()

    for i in range(20):
        cloud = Cloud()

        if cloud_list == []:
            cloud_list.append(cloud)
            cloud.draw(board.canvas, begin)
        else:
            for clouds in cloud_list:
                if abs(cloud.pos_y - clouds.pos_y) > 10:
                    if len(cloud_list) <= 20:
                        cloud_list.append(cloud)

    pit_presence_list = [(20, 25), (40, 46), (78, 82), (103, 109),
                         (144, 147), (169, 175), (196, 201), (225, 231)]

    while len(coin_list) != 50:
        coin = Coins()
        flag = True
        for p_i in pit_presence_list:
            if coin.pos_x >= p_i[0] and coin.pos_x <= p_i[1]:
                flag = False

        if flag:
            coin_list.append(coin)

    for i in range(len(pit_presence_list)):
        p_i = Pit()
        p_i.start = pit_presence_list[i][0]
        p_i.end = pit_presence_list[i][1]
        pit_list.append(p_i)

    enemy_path_list = [(26, 35), (53, 69), (90, 96), (148, 160), (203, 212)]

    obstacle_presence_list = [
        (47, 53), (83, 89), (112, 118), (131, 137), (183, 189), (215, 221)]

    for i in range(len(enemy_path_list)):
        enemy = Enemy()
        enemy.pos_x_start = enemy_path_list[i][0]
        enemy.pos_x_end = enemy_path_list[i][1]
        enemy.pos_x = enemy.pos_x_start
        enemy_list.append(enemy)

    for i in range(len(obstacle_presence_list)):
        obstacle = Obstacle()
        obstacle.pos_y = obstacle_presence_list[i][0]
        obstacle_list.append(obstacle)

    for i in range(NUM_COLS):
        flag = 1
        for obstacle in obstacle_list:
            if i >= obstacle.pos_y and i <= obstacle.pos_y + 6:
                flag = 0
                base_level[i] = -1 * (NUM_STONE_ROWS[0] - obstacle.pos_x)
        if flag == 0:
            continue

    os.system("aplay ./theme.wav &")
    while True:
        os.system("tput reset")
        boss.oscillate()
        boss.draw(board.canvas)

        mario.draw(board.canvas, begin, base_level[mario.pos[1] + begin[0]])
        print("score : " + str(score[0]) + "\tlives : " + str(lives))

        for cloud in cloud_list:
            cloud.draw(board.canvas, begin)

        for pit in pit_list:
            pit.draw(board.canvas)

        for coin in coin_list:
            if coin.check(mario, begin=begin):
                coin_list.remove(coin)
                score[0] += 1
                continue
            else:
                coin.draw(board.canvas, begin)

        for pit in pit_list:
            if pit.check_fall(mario, begin) is False:
                os.system("fuser -k -TERM ./theme.wav")
                start_screen()

        for obstacle in obstacle_list:
            # print(o.pos_y)
            obstacle.draw(board.canvas, begin)

        for enemy in enemy_list:
            enemy.draw(board.canvas)
            enemy.oscillate()
            if enemy.pos_x == begin[0] + \
                    mario.pos[1] and mario.legs_pos == enemy.pos_y:
                lives -= 1
                score[0] += 10
                enemy_list.remove(enemy)
                if lives == 0:
                    os.system("fuser -k -TERM ./theme.wav")
                    start_screen()
                else:
                    break
                # quit()
            elif enemy.pos_x == begin[0] + mario.pos[1] and mario.legs_pos + 1 == enemy.pos_y:
                enemy_list.remove(enemy)
                score[0] += 10

        if not boss.check_life():
            os.system("fuser -k -TERM ./theme.wav")
            game_end(score)

        board.draw(begin)
        mario.move_mario(
            args={
                "board" : board,
                "canvas" : board.canvas,
                "begin" : begin,
                "enemy_list" : enemy_list,
                "score" : score,
                "base_level" : base_level[mario.pos[1] + begin[0]],
                "base_level_next" : base_level[mario.pos[1] + begin[0] + 1],
                "base_level_prev" : base_level[mario.pos[1] + begin[0] - 1],
                "boss" : boss,
                "coin_list" : coin_list
            })


def start_screen():
    '''Start Screen For the Game'''
    os.system('tput reset')
    print(
        "\t\t\t\t\t\t\t\t" +
        Fore.RED +
        Back.BLUE +
        "Hello, Welcome To Mario2.0 !" +
        Back.BLACK)
    print(Fore.GREEN + Back.BLACK + "Press P to play")
    print(Fore.GREEN + Back.BLACK + "Press Q to quit")
    char = input()

    if char == 'p' or char == 'P':
        game_loop()
    else:
        quit()


def game_end(score):
    '''Stop The Game'''
    os.system('tput reset')
    print("\t\t\t\t\t\t\t\t" + Fore.RED + Back.BLUE +
          "Thanks For Playing Mario2.0 !" + Back.BLACK)
    print("\t\t\t\t\t\t\t\t" + Fore.RED + Back.BLUE +
          "Your Final score is " + str(score[0]) + Back.BLACK)
    print(Fore.GREEN + Back.BLACK + "Press P to play")
    print(Fore.GREEN + Back.BLACK + "Press Q to quit")

    char = input()
    if char == 'p' or char == 'P':
        game_loop()
    else:
        exit()
