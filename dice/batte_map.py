import game_framework
import main_map
from pico2d import *

mpa =None
def create_world():
    global map
    map = load_image('battle_map.png')

def destroy_world():
   pass

def enter():
    open_canvas(1200,680)
    create_world()



def exit():
    destroy_world()
    close_canvas()


def update():
   pass



def draw():
    global map

    clear_canvas()
    map.draw(600, 340)
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
                if count ==3:
                    game_framework.change_state(main_map)
                else:
                    count +=1


def pause(): pass


def resume(): pass