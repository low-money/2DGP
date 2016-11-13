import game_framework
from pico2d import *
import main_map

name = "Select_char"
image = None

from Character_Select_Class import Select_char1 ,Select_char2, Select_char3, Dice_a

select1 = None
select2 = None
select3 = None
dice = None
count =1
def create_world():
    global select1,select2,select3 , dice
    select1 = Select_char1()
    select2 = Select_char2()
    select3 = Select_char3()
    dice = Dice_a()

def destroy_world():
    global select1, select2, select3
    del(select1)
    del(select2)
    del(select3)

def enter():

    open_canvas(1200,680)
    create_world()



def exit():
    destroy_world()
    close_canvas()


def update():
   if count ==2:
       dice.update()
   if count ==3:
       Dice_a.frame = dice.frame



def draw():
    global select1, select2, select3 ,dice
    clear_canvas()
    if count ==1 :
        select1.draw()
        dice.draw()
    elif count ==2:
        select2.draw()
        dice.draw()
    elif count ==3:
        select3.draw()
        dice.draw()
    update_canvas()




def handle_events():
    global count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                if count ==3:
                    game_framework.change_state(main_map)
                else:
                    count +=1


def pause(): pass


def resume(): pass




