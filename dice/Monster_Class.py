from pico2d import*
import random

class Monkey1:
    def __init__(self):
        self.image = load_image('monkey.png')
    def draw(self):
        self.image.clip_draw(0, 3 * 65, 50, 60, 550, 120)


class Monkey2:
    def __init__(self):
        self.image = load_image('monkey.png')
    def draw(self):
        self.image.draw()

class Monkey3:
    def __init__(self):
        self.image = load_image('monkey.png')
    def draw(self):
        self.image.draw()