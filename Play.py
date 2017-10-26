import tkinter as t
import os

win=t.Tk();

frame=t.Frame(win,width=200,height=200,background="#fffBBB")
frame.pack(fill=None, expand=True)

def runFaceDetection():
   os.system('faceDetect.py')

playButton = t.Button(win, text ="Open Camera", command = runFaceDetection)

playButton.pack()
