from pico2d import*
import random


class Fighter:

    def __init__(self):
        self.mn = 0
        self.mc =0
        self.x = 600
        self.y = 90
        self.frame3 =2
        self.image = load_image('fighter.png')
    def draw(self):
        self.image.clip_draw(0 , self.frame3 *65, 50, 60, self.x, self.y)
    def update(self):
        self.mc += 1
        if(self.y > 305):
                self.frame3 = 1
        if(self.mc % 32 >= 24):
            self.frame3 =2

        if(0 < self.mc % 32 <= 8):
           self.x -= 52
           self.y += 33
        elif(8< self.mc %32 <=16):
            self.x += 52
            self.y += 33
        elif(16< self.mc %32 <=24):
            self.x+=52
            self.y -= 33
        elif(24< self.mc %32 or self.mc %32 ==0):
            self.x -= 52
            self.y -= 33
        if self.mc % 32 == 8:
            self.x = 160
            self.y = 370
        elif self.mc %32 == 0:
            self.x = 600
            self.y = 90
        elif self.mc %32 == 16:
            self.x = 600
            self.y = 620
        elif self.mc % 32 ==24:
            self.x = 1070
            self.y = 340
class Lin:
    def __init__(self):
        self.mn = 0
        self.mc =0
        self.x = 600
        self.y = 90
        self.frame4 =2
        self.image = load_image('lin.png')
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0
    def draw(self):
        self.image.clip_draw(0 , self.frame4 *65, 50, 60, self.x, self.y)
    def update(self,frame_time):
        self.mc += 1

        if(self.y > 305):
            self.frame4 = 1
        if(self.mc % 32 >= 24):
            self.frame4 =2

        if(0 < self.mc % 32 <= 8):
           self.x -= 52
           self.y += 33
        elif(8< self.mc %32 <=16):
            self.x += 52
            self.y += 33
        elif(16< self.mc %32 <=24):
            self.x+=52
            self.y -= 33
        elif(24< self.mc %32 or self.mc %32 ==0):
            self.x -= 52
            self.y -= 33
        if self.mc % 32 == 8:
            self.x = 160
            self.y = 370
        elif self.mc %32 == 0:
            self.x = 600
            self.y = 90
        elif self.mc %32 == 16:
            self.x = 600
            self.y = 620
        elif self.mc % 32 ==24:
            self.x = 1070
            self.y = 340
class Smasu:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    def __init__(self):
        self.mn = 0
        self.mc =0
        self.x = 600
        self.y = 90
        self.frame3 =2
        self.image = load_image('smasu.png')
    def draw(self):
        self.image.clip_draw(0 , self.frame3 *65, 50, 60, self.x, self.y)
    def update(self):
        self.mc += 1

        if(self.y > 305):
                self.frame3 = 1
        if(self.mc % 32 >= 24):
            self.frame3 =2

        if(0 < self.mc % 32 <= 8):
           self.x -= 52
           self.y += 33
        elif(8< self.mc %32 <=16):
            self.x += 52
            self.y += 33
        elif(16< self.mc %32 <=24):
            self.x+=52
            self.y -= 33
        elif(24< self.mc %32 or self.mc %32 ==0):
            self.x -= 52
            self.y -= 33
        if self.mc % 32 == 8:
            self.x = 160
            self.y = 370
        elif self.mc %32 == 0:
            self.x = 600
            self.y = 90
        elif self.mc %32 == 16:
            self.x = 600
            self.y = 620
        elif self.mc % 32 ==24:
            self.x = 1070
            self.y = 340