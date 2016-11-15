from pico2d import*
import random


class Box1:
    def __init__(self):
        self.image = load_image('item_box.png')
        self.pos = 19
        self.state = 105
        self.state2 = 160
    def draw(self):
        self.image.clip_draw(0, self.state, 50, 50, 200, 530)

class Box2:
    def __init__(self):
        self.image = load_image('item_box.png')
        self.pos = 19
        self.state = 160
    def draw(self):
        self.image.clip_draw(0, self.state, 50, 50, 400, 530)


class Box3:
    def __init__(self):
        self.image = load_image('item_box.png')
        self.pos = 19
        self.state = 160
    def draw(self):
        self.image.clip_draw(0, self.state, 50, 50, 800, 530)