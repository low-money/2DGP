from pico2d import *

import All_Class
import Character_Class



def handle_events():
    global running
    global turn
    global dice_count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE) :
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            dice_count +=1

open_canvas(1200,680)
player =0
player1 = Character_Class.Fighter()
map1= All_Class.Map_board()
dice_L = All_Class.Dice_L()
dice_R = All_Class.Dice_R()
dice_a = All_Class.Dice_a()
dice_back = All_Class.Dice_Back1()
dice_back2 = All_Class.Dice_Back2()
select_char1 = All_Class.Select_char1()
select_char2 = All_Class.Select_char2()
select_char3 = All_Class.Select_char3()

fighter = Character_Class.Fighter()
lin = Character_Class.Lin()
smasu = Character_Class.Smasu()
dice_count = 1
turn_count = -1
char_turn = 0
i = 0
turn = False
running = True
select_char = True

while running:
    handle_events()
    clear_canvas()
    map1.draw()

    if select_char == True:
        if dice_count %2 ==0 and turn_count == -1:
            select_char2.draw()
            dice_a.update()
            dice_a.draw()
        elif dice_count ==1 and turn_count ==-1:
            select_char1.draw()
            dice_a.draw()
        elif dice_count %3 == 0:
            select_char3.draw()
            dice_a.draw()
            if dice_a.frame ==1 or dice_a.frame ==0:
                player = 1
                player1= smasu
                turn_count = 0
            elif dice_a.frame ==2 or dice_a.frame ==3:
                player = 1
                player1= lin
                turn_count = 0
            elif dice_a.frame ==4 or dice_a.frame ==5:
                player = 1
                turn_count = 0
        elif player !=0:
            select_char = False
            dice_count = -1

    else:
        if turn_count != -1 and dice_count % 2 == 0:
            dice_L.update()
            dice_R.update()
            i = 0
            turn_count = 0
            dice_back2.draw()

        elif turn_count != -1 and dice_count % 2 != 0:
            if dice_count != -1:
                  player1.mn = dice_L.frame1 + dice_R.frame2 + 2
                  lin.mn = dice_L.frame1 + dice_R.frame2 + 2

            if (turn_count == 0):
                turn_count = 1
            dice_back.draw()

        if (turn_count == 1 and char_turn == 0):
            char_turn = 0
            while (i < player1.mn):
                clear_canvas()

                player1.update()
                i += 1

                map1.draw()
                player1.draw()


                update_canvas()
                delay(0.2)


        elif turn_count == 1 and char_turn != 0:
            char_turn = 0
            while (i < lin.mn):
                clear_canvas()

                lin.update()

                map1.draw()
                lin.draw()
                player1.draw()
                i += 1

                update_canvas()
                delay(0.2)

        dice_L.draw()
        dice_R.draw()
        player1.draw()

    update_canvas()

    delay(0.05)





close_canvas()


