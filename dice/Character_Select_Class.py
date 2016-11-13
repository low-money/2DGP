from pico2d import *
import random
class Select_char1:
    def __init__(self):
        self.image = load_image('select_char1.png')
    def draw(self):
        self.image.draw(600,300)
class Select_char2:
    def __init__(self):
        self.image = load_image('select_char2.png')
    def draw(self):
        self.image.draw(600,300)
class Select_char3:
    def __init__(self):
        self.image = load_image('select_char3.png')
    def draw(self):
        self.image.draw(600,300)

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