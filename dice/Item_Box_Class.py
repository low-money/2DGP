from pico2d import*
import random


class Box1:
    def __init__(self):
        self.image = load_image('item_box.png')
        self.pos = 9
        self.state = 160
        self.state2 = 160
    def draw(self):
        self.image.clip_draw(0, self.state, 50, 50, 220, 380)
    def draw2(self):
        self.image.clip_draw(0, 105, 50, 50, 220, 380)

class Box2:
    def __init__(self):
        self.image = load_image('item_box.png')
        self.pos = 4
        self.state = 160
    def draw(self):
        self.image.clip_draw(0, self.state, 50, 50, 380, 200)
    def draw2(self):
        self.image.clip_draw(0, 105, 50, 50, 380, 200)


class Box3:
    def __init__(self):
        self.image = load_image('item_box.png')
        self.pos = 18
        self.state = 160
    def draw(self):
        self.image.clip_draw(0, self.state, 50, 50, 720, 540)
    def draw2(self):
        self.image.clip_draw(0, 105, 50, 50, 720, 540)
class Box4:
    def __init__(self):
        self.image = load_image('item_box.png')
        self.pos = 30
        self.state = 160
    def draw(self):
        self.image.clip_draw(0, self.state, 50, 50, 720, 140)
    def draw2(self):
        self.image.clip_draw(0, 105, 50, 50, 720, 140)