# 3RD UMPIRE DECISION REVIEW SYSTEM (DRS)

import tkinter 
import pandas
import PIL.Image  , PIL.ImageTk
import cv2
from functools import partial
import threading
import imutils
import time

stream = cv2.VideoCapture('clip.mp4.mp4')
flag = True
# Functions for display video playback according to the button

def play(speed): 
    global flag
    print(f"Video play at Speed : {speed}")
    
    # Play video in reverse/forward mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES , frame1 + speed)
    
    grabbed , frame = stream.read()
    if not grabbed:                         
        exit()
    frame = imutils.resize(frame , width = SET_WIDTH , height= SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0 , image = frame , anchor = tkinter.NW)
    if flag:
        canvas.create_text(135 , 25 , fill = 'black', font="Times 20 bold" , text = "Decision Pending")
    flag = not flag
def pending(decision):
    # 1. Display decison pending
    frame = cv2.cvtColor(cv2.imread("des.png") , cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame , width = SET_WIDTH , height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0 , image =  frame, anchor = tkinter.NW)
    # 2. Wait for a second
    time.sleep(2)
    # 3. Display sponser
    frame = cv2.cvtColor(cv2.imread("sponser.png") , cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame , width = SET_WIDTH , height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0 , image = frame, anchor = tkinter.NW)
    # 4. Wait for 2 second
    time.sleep(2)
    # 5. Display out/not out 
    if decision == 'OUT':
        decisionImg = 'out.png' 
    else:
         decisionImg = 'not_out.png'
    
    frame = cv2.cvtColor(cv2.imread(decisionImg) , cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame , width = SET_WIDTH , height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0 , image = frame, anchor = tkinter.NW)
def out():
    thread = threading.Thread(target=pending , args=("OUT",))
    thread.daemon = 1
    thread.start()
    print("OUT")

def not_out():
    thread = threading.Thread(target=pending , args=("NOT OUT",))
    thread.daemon = 1
    thread.start()
    print("NOT OUT")
# Setting  width and height for my software's main screen

SET_WIDTH = 480
SET_HEIGHT = 360

# Creting window for my tkinter or tkinter gui starts here

window = tkinter.Tk()
window.title("YashXDS ""3\u02b3\u1d48" + "Umpire DRS Kit")
window.iconbitmap('S:\MAIN PROJECTS\PYTHON PROJECT\\throw.ico')

cv_img = cv2.cvtColor(cv2.imread("welcome1.png"), cv2.COLOR_BGR2RGB)         #import welcome screen
canvas = tkinter.Canvas(window , width= SET_WIDTH , height= SET_HEIGHT)    #our canvas

photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))          #read img in array
img_on_canvas = canvas.create_image(0,0, anchor = tkinter.NW , image = photo)   #adding image into the canvas
canvas.pack()

# Buttons to control Playback
btn = tkinter.Button(window , text='\u23EA Previous Slow' , width = 50 , command = partial(play , -2))
btn.pack()

btn = tkinter.Button(window , text='\u23EA Previous Fast' , width = 50 , command = partial(play , -25))
btn.pack()

btn = tkinter.Button(window , text='Next Slow \u23EA' , width = 50 , command = partial(play , 2))
btn.pack()

btn = tkinter.Button(window , text='Next Fast \u23EA' , width = 50 , command = partial(play , 25))
btn.pack()

btn = tkinter.Button(window , text='\U0001F636 OUT \U0001F636' , width = 50 , command = out )
btn.pack()

btn = tkinter.Button(window , text='NOT \U0001F601 OUT' , width = 50 , command = not_out)
btn.pack()
window.mainloop()
