import game_framework

import json
import battle_map

from pico2d import *

from All_Class import Map_board ,Dice_L , Dice_R ,Dice_Back1, Dice_Back2

from Character_Select_Class import Dice_a

from Character_Class import Fighter ,Lin , Smasu

from Item_Box_Class import Box1 ,Box2,Box3 ,Box4

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
box1 = None
box2 = None
box3 = None
box4 = None
item = None
x=0
y=0
mc =0
count =0
move_count = 0
turn = 1
i=0
mnum =0
inum = 0
def create_world():
    global map, player, dice_c, dice_l, dice_r,  dice_back, dice_back2, monkey1,monkey2,monkey3,boar1,boar2,boar3 , monster , box1, box2, box3,box4, item

    dice_c = Dice_a()
    dice_l = Dice_L()
    dice_r = Dice_R()
    dice_back = Dice_Back1()
    dice_back2 =Dice_Back2()
    monkey1 = Monkey1()
    monkey2 = Monkey2()
    monkey3 = Monkey3()
    boar1 = Boar1()
    boar2 = Boar2()
    boar3 = Boar3()
    monster  = [monkey1 , monkey2, monkey3,boar1,boar2,boar3]
    box1 = Box1()
    box2 = Box2()
    box3 = Box3()
    box4 = Box4()
    item= [box1,box2,box3,box4]
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
    global font
    open_canvas(1200,680)
    font = load_font('ENCR10B.TTF')
    create_world()

def exit():

    close_canvas()

def update():
    global i, player, dice_l,dice_r,move_count , turn

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
                font.draw(550, 450, 'Turn: %3.2d' % turn)
                font.draw(500,340, 'Dice number: %3.2d' % player.mn)
                mnum = 0
                inum = 0
                while mnum < len(monster):
                    if monster[mnum].life ==1:
                        monster[mnum].draw()
                    mnum += 1
                while inum < len(item):
                    item[inum].draw()
                    inum += 1
                update_canvas()
                delay(0.2)
            move_count =0
def draw():
    global player , mpa, dice_l, dice_r , dice_back, dice_back2, monster ,mnum,inum , item,font ,x ,y,mc
    clear_canvas()
    map.draw()
    player.draw()
    font.draw(550, 450, 'Turn: %3.2d' % turn)
    mnum=0
    inum =0

    while mnum < len(monster):
        if player.mc % 32 == monster[mnum].pos and monster[mnum].life ==1:
            if( monster[mnum].pos == 1 or monster[mnum].pos == 13 or monster[mnum].pos == 19 )and monster[mnum].life ==1 :
                monster[mnum].life = 0
                m = open('monster_state.txt', 'w')
                mon = {'monster': 1, "HP": 20}
                json.dump(mon, m)
                m.close()

            elif (monster[mnum].pos == 6 or monster[mnum].pos == 10 or monster[mnum].pos == 22 )and monster[mnum].life ==1:
                monster[mnum].life = 0
                m = open('monster_state.txt', 'w')
                mon = {'monster': 2, "HP": 25}
                json.dump(mon, m)
                m.close()
            x = player.x
            y = player.y
            mc = player.mc
            game_framework.push_state(battle_map)
        monster[mnum].draw()
        mnum+=1
    while inum < len(item):
        if player.mc %32== item[inum].pos:
            item[inum].draw2()
        else:
            item[inum].draw()
        inum+=1

    if count %2 ==0:
        dice_back.draw()

    else:
        dice_back2.draw()
    dice_l.draw()
    dice_r.draw()
    update_canvas()

def handle_events():
    events = get_events()
    global count ,turn
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                turn += 0.5
                count +=1


def pause(): pass


def resume(): pass




