import game_framework
import main_map
import json
from pico2d import *
from Character_Class import Fighter ,Lin , Smasu
from Monster_Class import Monkey, Boar
from All_Class import Dice_L , Dice_R ,Dice_Back1, Dice_Back2
map =None
player = None
monster = None
dice_l = None
dice_r = None
dice_back= None
dice_back2 = None
def create_world():
    global map , player,monster , dice_l, dice_r,  dice_back, dice_back2 ,play ,mon
    f = open('select_char.txt', 'r')
    select = json.load(f)
    f.close()
    if select['character'] == 0 or select['character'] == 1:
        player = Smasu()
    elif select['character'] == 2 or select['character'] == 3:
        player = Lin()
    elif select['character'] == 4 or select['character'] == 5:
        player = Fighter()
    m = open('monster_state.txt', 'r')
    mon = json.load(m)
    m.close()
    p = open('player_state.txt','r')
    play = json.load(p)
    p.close()
    if mon["monster"] == 1:
        monster = Monkey()
    else:
        monster = Boar()
    map = load_image('battle_map.png')
1
def destroy_world():
   pass

def enter():
    global font
    open_canvas(640,480)
    font = load_font('ENCR10B.TTF')
    create_world()



def exit():
    destroy_world()
    close_canvas()


def update():
   pass



def draw():
    global map , player ,font,play,mon

    clear_canvas()
    map.draw(320, 240)
    player.x = 150
    player.y = 300
    player.frame = 1
    player.draw()
    monster.draw()
    font.draw(110, 90, 'HP: %3.2d' % play["HP"])
    font.draw(470, 90, 'HP: %3.2d' % mon["HP"])

    update_canvas()




def handle_events():
    pass
    global count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                    game_framework.push_state(main_map)



def pause(): pass


def resume(): pass