import game_framework
from pico2d import *

import char_select
import main_map


name = "TitleState"
image = None

def enter():
    global image
    image = load_image('title.png')

def exit():
    global image
    del(image)


def pause():
    pass

def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(char_select)



def update():
    pass


def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()



