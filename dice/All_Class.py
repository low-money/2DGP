from pico2d import*
import random


class Map_board:
    def __init__(self):
        self.image = load_image('map1.png')
    def draw(self):
        self.image.draw(600,340)

class Dice_L:

    def __init__(self):

        self.x = 570
        self.y = 340
        self.frame1 =0
        self.image = load_image('dice.png')
    def draw(self):
        self.image.clip_draw(self.frame1 * 100 + 20, 20, 60, 60, self.x, self.y)
    def update(self):
        self.frame1 = random.randint(0, 5)


class Dice_R:
    def __init__(self):
        self.x = 630
        self.y = 340
        self.frame2 = 0
        self.image = load_image('dice.png')
    def draw(self):
        self.image.clip_draw(self.frame2 * 100 + 20, 20, 60, 60, self.x, self.y)
    def update(self):
        self.frame2 = random.randint(0, 5)
class Dice_a:
    def __init__(self):
        self.x = 600
        self.y = 400
        self.frame = 0
        self.image = load_image('dice.png')
    def draw(self):
        self.image.clip_draw(self.frame * 100 + 20, 20, 60, 60, self.x, self.y)
    def update(self):
        self.frame = random.randint(0, 5)

class Dice_Back1:
    def __init__(self):
        self.image = load_image('dice_back.png')
    def draw(self):
        self.image.draw(600,300)

class Dice_Back2:
    def __init__(self):
        self.image = load_image('dice_back2.png')
    def draw(self):
        self.image.draw(600,300)


