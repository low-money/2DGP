from pico2d import*
import random
class Monkey:
    def __init__(self):
        self.image = load_image('monkey.png')
        self.life = 1
        self.pos = 19
        self.x =0
        self.y = 0
    def draw(self):
        self.image.clip_draw(0, 3 * 65, 50, 60, 500, 300)

class Monkey1:
    def __init__(self):
        self.image = load_image('monkey.png')
        self.life = 1
        self.pos = 19
        self.x =0
        self.y = 0
    def draw(self):
        self.image.clip_draw(0, 3 * 65, 50, 60, 800, 530)


class Monkey2:
    def __init__(self):
        self.image = load_image('monkey.png')
        self.life = 1
        self.pos = 1
    def draw(self):
        self.image.clip_draw(50, 3 * 65, 50, 60, 510, 110)

class Monkey3:
    def __init__(self):
        self.image = load_image('monkey.png')
        self.life = 1
        self.pos = 13
    def draw(self):
        self.image.clip_draw(0, 3 * 65, 50, 60, 460, 520)
class Boar:
    def __init__(self):
        self.image = load_image('boar.png')
        self.life = 1
        self.pos = 10
        self.x =0
        self.y =0
    def draw(self):
        self.image.clip_draw(0, 4 * 65, 80, 60, 500, 300)
class Boar1:
    def __init__(self):
        self.image = load_image('boar.png')
        self.life = 1
        self.pos = 10
        self.x =0
        self.y =0
    def draw(self):
        self.image.clip_draw(0, 4 * 65, 80, 60, 290, 410)
class Boar2:
    def __init__(self):
        self.image = load_image('boar.png')
        self.life = 1
        self.pos = 22
    def draw(self):
        self.image.clip_draw(0, 4 * 65, 80, 60, 950, 420)
class Boar3:
    def __init__(self):
        self.image = load_image('boar.png')
        self.life = 1
        self.pos = 6
    def draw(self):
        self.image.clip_draw(90, 4 * 65, 80, 60, 250, 260)