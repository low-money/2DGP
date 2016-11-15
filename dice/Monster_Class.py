from pico2d import*
import random

class Monkey1:
    def __init__(self):
        self.image = load_image('monkey.png')
        self.life = 1
        self.pos = 19
    def draw(self):
        self.image.clip_draw(0, 3 * 65, 50, 60, 800, 530)


class Monkey2:
    def __init__(self):
        self.image = load_image('monkey.png')
    def draw(self):
        self.image.clip_draw(50, 3 * 65, 50, 60, 510, 110)

class Monkey3:
    def __init__(self):
        self.image = load_image('monkey.png')
    def draw(self):
        self.image.clip_draw(0, 3 * 65, 50, 60, 550, 520)

class Boar1:
    def __init__(self):
        self.image = load_image('boar.png')
    def draw(self):
        self.image.clip_draw(0, 4 * 65, 80, 60, 300, 300)
class Boar2:
    def __init__(self):
        self.image = load_image('boar.png')
    def draw(self):
        self.image.clip_draw(0, 4 * 65, 80, 60, 900, 420)
class Boar3:
    def __init__(self):
        self.image = load_image('boar.png')
    def draw(self):
        self.image.clip_draw(0, 4 * 65, 80, 60, 250, 200)