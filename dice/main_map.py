import game_framework

import json
from pico2d import *

from All_Class import Map_board ,Dice_L , Dice_R ,Dice_Back1, Dice_Back2

from Character_Select_Class import Dice_a

from Character_Class import Fighter ,Lin , Smasu

from Monster_Class import Monkey1 , Monkey2, Monkey3 ,Boar1, Boar2, Boar3

map = None
player = None
dice_c = None
dice_l = None
dice_r = None
dice_back= None
dice_back2 = None
monkey1 = None
monkey2 = None
monkey3 = None
boar1 = None
boar2 = None
boar3 = None
monster = None
count =0
move_count = 0
i=0
j=0
def create_world():
    global map, player, dice_c, dice_l, dice_r,  dice_back, dice_back2, monkey1,monkey2,monkey3,boar1,boar2,boar3 , monster
    dice_l = Dice_L()
    dice_r = Dice_R()
    dice_c = Dice_a()
    dice_back = Dice_Back1()
    dice_back2 =Dice_Back2()
    monkey1 = Monkey1()
    monkey2 = Monkey2()
    monkey3 = Monkey3()
    boar1 = Boar1()
    boar2 = Boar2()
    boar3 = Boar3()
    monster  = [monkey1 , monkey2, monkey3,boar1,boar2,boar3]
    f = open('select_char.txt', 'r')
    select = json.load(f)
    f.close()
    if select['character'] == 0 or select['character'] ==  1:
        player = Smasu()
    elif select['character'] == 2 or select['character'] ==  3:
        player = Lin ()
    elif select['character'] == 4 or select['character'] ==  5:
        player = Fighter()
    map =Map_board()


def destroy_world():
    global map, player
    del(map)
    del(player)


def enter():
    open_canvas(1200,680)
    create_world()

def exit():

    close_canvas()

def update():
    global i, player, dice_l,dice_r,move_count
    if count %2 !=0 and move_count ==0:
        dice_l.update()
        dice_r.update()
        i=0
        player.mn = dice_l.frame1 + dice_r.frame2 + 2

    else:
        move_count = 1
        if count % 2 == 0 and move_count == 1:

            while( i <player.mn):
                clear_canvas()
                player.update()
                i += 1
                map.draw()
                player.draw()
                j = 0
                while j < len(monster):
                    monster[j].draw()
                    j += 1
                update_canvas()
                delay(0.2)
            move_count =0

    if player.mn == monkey1.pos :
        if monkey1.life ==0:
            monkey1.remove(monkey1)



def draw():
    global player , mpa, dice_l, dice_r , dice_back, dice_back2, monster ,j
    clear_canvas()
    map.draw()
    player.draw()
    j=0
    while j < len(monster):
        monster[j].draw()
        j+=1

    if count %2 ==0:
        dice_back.draw()
    else:
        dice_back2.draw()
    dice_l.draw()
    dice_r.draw()
    update_canvas()

def handle_events():
    events = get_events()
    global count
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                count +=1


def pause(): pass


def resume(): pass




