import cv2 as cv
import numpy as np
import pyautogui
import time
from threading import Thread
import serial

arduinoData = serial.Serial('COM4',115200)

thres = .60
gnote = 6
gnote1 = str(gnote)
rnote = 7
rnote = str(rnote)
ynote = 8
ynote = str(ynote)

class NotePlayer:
    def __init__(self, main_player) -> None:
        self.main_player = main_player
        self.note_image_g = cv.imread('photo/green_note2.png')
        self.note_image_r = cv.imread('photo/rednote2.png')
        self.note_image_y = cv.imread('photo/ye11_note.png')
        
    def find_g(self):
        time.sleep(.01) #orginal .025
        screenshot1 =self.main_player.screenshot
        screenshot1 = np.array(screenshot1)
           
        G_location = cv.matchTemplate(screenshot1, self.note_image_g,cv.TM_CCOEFF_NORMED)
        G_loc_array = np.array(G_location)
        min_val, max_val,min_loc,max_loc = cv.minMaxLoc(G_loc_array)
        g_max_val = max_val
        #print(g_max_val)
        #cv.imshow("match Template", G_loc_array)
        #cv.waitKey(1)

        if(g_max_val> thres):
            print("Green: ",g_max_val)
            arduinoData.write(bytes(gnote1, 'utf-8'))
            print(arduinoData.readline())
  

            
    def find_r(self):
        time.sleep(.01)
        screenshot1 =self.main_player.screenshot
        screenshot1 = np.array(screenshot1)
        r_location = cv.matchTemplate(screenshot1, self.note_image_r,cv.TM_CCOEFF_NORMED)
        r_loc_array = np.array(r_location)
        min_val, max_val,min_loc,max_loc = cv.minMaxLoc(r_loc_array)
        r_max_val = max_val


        if(r_max_val> thres):
            #print("Red: ",r_max_val)
            arduinoData.write(bytes(rnote, 'utf-8'))
            print(arduinoData.readline())

           

    def find_y(self):
        time.sleep(.01)
        screenshot1 =self.main_player.screenshot
        screenshot1 = np.array(screenshot1)
    
        #print("match")
        y_location = cv.matchTemplate(screenshot1, self.note_image_y,cv.TM_CCOEFF_NORMED)
        y_loc_array = np.array(y_location)
        min_val, max_val,min_loc,max_loc = cv.minMaxLoc(y_loc_array)
        y_max_val = max_val
        #print(y_max_val)
        #cv.imshow("match Template", y_loc_array)
        #cv.waitKey(1)
        if(y_max_val> thres):
            print("Yellow: ",y_max_val)
            arduinoData.write(bytes(ynote, 'utf-8'))
            print(arduinoData.readline())
  
                     

    def run(self):
        while True:
            self.find_g()
            self.find_r()
            self.find_y()


