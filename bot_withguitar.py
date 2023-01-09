import numpy as np
import cv2 as cv
import time
from PIL import Image, ImageGrab
from threading import Thread
from note_withguitar.note_player_withguitar import NotePlayer

class MainPlayer:
    def __init__(self) -> None:
        self.player = []
        self.screenshot = None 
        self.sshsv = None
        print("Main Player complete")
        
def update_screen(player):
    t0 = time.time()
    while True:
        player.screenshot = ImageGrab.grab()                               #takescreen shot
        player.screenshot = np.array(player.screenshot)
        player.screenshot = player.screenshot[750:950,900:1350]             #vales for no guitar
        #player.screenshot = player.screenshot[450:650,900:1350]
        player.screenshot = cv.cvtColor(player.screenshot,cv.COLOR_RGB2BGR)
        #player.sshsv = cv.cvtColor(player.screenshot,cv.COLOR_BGR2HSV)    

        #cv.imshow("CV", player.screenshot)
       # key = cv.waitKey(1)
        #if key == ord('a'):
        #    break
        #ex_time = time.time() - t0
        #print("FPS : " , 1/ex_time)
        #print("image")
        #t0 = time.time()
        time.sleep(.05) #original .1

def start_bot():
    print("-Press z to starrt program")
    print("-Press x to exit")


if __name__ == "__main__":
    main_player = MainPlayer()
    
    start_bot()
    while True:
        user_input = input()
        if user_input == "z":
                screen_task = Thread(target = update_screen, args = (main_player,),daemon = True)
                screen_task.start()
                print("thread started")
                note_player = NotePlayer(main_player)
                note_player.run()
                
        elif user_input == "c":
            note_player = NotePlayer(main_player)
            note_player.run()
            

        elif user_input == "x":
            cv.destroyAllWindows()
            break
        else:
            print("error")

    print("Bot terminated")        

