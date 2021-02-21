import cv2
import numpy as np
import pyautogui
from random import randint
import os
from tkinter import *
from tkinter import messagebox
from time import sleep

screen_size = (1920,1080)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
rand = randint(0, 10000000000)
while f'recorder {rand}.avi' in os.listdir():
    rand = randint(0, 10000000000)
out = cv2.VideoWriter(f'recorder {rand}.avi', fourcc, 20.0, (screen_size))


def btn():
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        out.write(frame)
        cv2.imshow("VRECORDER SHOW",frame)
        if cv2.waitKey(1) == ord("q"):
            break
def btn2():
    root.destroy()
    
root = Tk()
root.title('VRECORDER')
root.geometry('400x250')
root['bg'] = 'white'
Button(root, text = 'Start Record', command = btn, bg = 'Red', fg = 'white', font = 'Arial 25').pack()
Label(root, bg = 'blue', fg = 'white', font = 'Arial 25', text = 'Press Q to stop!').pack()
Button(root, text = 'Exit', command = btn2, bg = 'Red', fg = 'white', font = 'Arial 25').pack()
root.mainloop()