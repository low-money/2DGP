import game_framework

from pico2d import *

from All_Class import Map_board ,Dice_L , Dice_R ,Dice_Back1, Dice_Back2

from Character_Select_Class import Dice_a

from Character_Class import Fighter ,Lin , Smasu


map = None
player = None
dice_c = None
dice_l = None
dice_r = None
count =0
dice_back= None
dice_back2 = None
def create_world():
    global map, player, dice_c, dice_l, dice_r,  dice_back, dice_back2
    dice_l = Dice_L()
    dice_r = Dice_R()
    dice_c = Dice_a()
    dice_back = Dice_Back1()
    dice_back2 =Dice_Back2()

    if dice_c.frame == 0 or 1:
        player = Smasu()
    elif dice_c.frame == 2 or 3:
        player = Lin ()
    elif dice_c.frame == 4 or 5:
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
    if count %2 !=0:
        dice_l.update()
        dice_r.update()
    else:
        player.mn = dice_l.frame1 + dice_r.frame2 + 2
    player.update()

def draw():
    global player , mpa, dice_l, dice_r , dice_back, dice_back2
    clear_canvas()
    map.draw()
    player.draw()

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




