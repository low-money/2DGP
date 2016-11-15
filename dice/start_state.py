import game_framework
from pico2d import *
import pico2d

import title_state
name = "StartState"
image = None
logo_time = 0.0
pico2d.open_canvas()

def enter():
    global image
    image = load_image('kpu_credit.png')


def exit():
    global image
    del(image)

def update():
    global name
    global logo_time

    if (logo_time > 0.5):
        logo_time = 0
        game_framework.push_state(title_state)
        #game_framework.quit()
    logo_time += 0.1

def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()


def pause(): pass
def resume(): pass