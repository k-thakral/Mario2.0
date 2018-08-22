import os
from colorama import init, Fore, Back

from manage import BOARD, MARIO, NUM_STONE_ROWS, NUM_COLS, cloud_list, obstacle_list, begin, enemy_list, base_level, SCORE, pit_list


init()
def GameLoop(LIVES = 2, SCORE = [0]):
    os.system("cvlc --play-and-exit ./theme.mp3 &")
    while True:
        os.system("tput reset")
        # print(base_level)
        #print(base_level[begin[0] + MARIO.pos[1]])
        MARIO.draw(BOARD.canvas, begin, base_level[MARIO.pos[1] + begin[0]])
        print("Score : " + str(SCORE[0]) + "\tLives : " + str(LIVES))

        for c in cloud_list:
            c.draw(BOARD.canvas, begin)

        for p in pit_list:
            p.draw(BOARD.canvas)

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
                if LIVES == 0:
                    start_screen()
                #quit()
            elif e.pos_x == begin[0] + MARIO.pos[1] and MARIO.legs_pos + 1 == e.pos_y:
                enemy_list.remove(e)
                SCORE[0] += 10

        BOARD.draw(begin)
        MARIO.move_mario(BOARD, BOARD.canvas, begin, enemy_list, SCORE,
                         base_level[MARIO.pos[1] + begin[0]], base_level[MARIO.pos[1] + begin[0] + 1], base_level[MARIO.pos[1] + begin[0] - 1])

def start_screen():
    print("\t\t\t\t\t\t\t\t" + Fore.RED + Back.BLUE + "Hello, Welcome To Mario2.0 !" + Back.BLACK)
    print(Fore.GREEN + Back.BLACK + "Press P to play")
    print(Fore.GREEN + Back.BLACK + "Press Q to quit")
    x = input()

    if x == 'p' or x == 'P':
        #base_level = 0
        SCORE[0] = 0
        MARIO.pos[0] = NUM_STONE_ROWS[0] - 2
        MARIO.pos[1] = 5
        GameLoop()
    else:
        quit()  

start_screen()
