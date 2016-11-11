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
    def draw(self):
        self.image.clip_draw(0 , self.frame4 *65, 50, 60, self.x, self.y)
    def update(self):
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