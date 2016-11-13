import game_framework

from pico2d import *

from All_Class import Map_board
import Character_Class

map = None

def create_world():
    global map

    map =Map_board()


def destroy_world():
    global boy, grass, balls, big_balls

    del(boy)
    del(balls)
    del(grass)
    del(big_balls)

def enter():
    global  image
    open_canvas(1200,680)

    create_world()


def exit():
    global image
    del(image)
    close_canvas()


def update():
    pass


def draw():
    global image
    clear_canvas()
    map.draw()
    update_canvas()




def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                pass


def pause(): pass


def resume(): pass




