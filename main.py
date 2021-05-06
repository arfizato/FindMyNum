from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
from random import * 
import random as rand

def goHigher():
    global guess, Min, Max
    Min=guess+1
    guess=rand.randint(Min,Max)
    compTxt.set(str(guess))

def goLower():
    global guess, Min, Max
    Max=guess-1
    guess=rand.randint(Min,Max)
    compTxt.set(str(guess))

def justRight():
    global stopPlaying, guess
    box = messagebox.askquestion("Your Number Is "+str(guess),"Do You Want To Stop Playing ?",icon="question")
    if box=="yes":
        stopPlaying=TRUE
    root.destroy()

def ClickedOnce(guess):
    compTxt.set(str(guess))
    tooLow["state"]=NORMAL
    tooHigh["state"]=NORMAL
    right["state"]=NORMAL

stopPlaying= FALSE
while stopPlaying== FALSE:    
    root= tk.Tk()
    root.title("flippity flip")
    root.iconbitmap(r'images/camera.ico')
    CompGenFont= font.Font(family="Times",size=20,weight="bold",slant="italic")
    TextFont= font.Font(family="Times",weight="bold")

    global guess, Min, Max 
    Min=0
    Max=1000
    guess=rand.randint(Min,Max)

    #defining the buttons
    compTxt = tk.StringVar()
    computer= Button(root,textvariable=compTxt,width=28,height=5,fg="#000",bg="#808080",activebackground="#808080",command= lambda : ClickedOnce(guess)  )
    computer.grid(row=1,column=0,columnspan=3)
    #computer["state"]=DISABLED
    computer["relief"]="sunken"
    compTxt.set("Choose a number in 0-1000 \nClick Me To Generate \nThe First Number")
    computer["font"]=CompGenFont

    tooLow= Button(root,width=15,height=5,text="Too Low!",bg="#004080",activebackground="#0057ae",command= goHigher)
    tooLow.grid(row=2,column=0)
    tooLow["font"]=TextFont
    tooLow["state"]=DISABLED

    right= Button(root,width=18,height=5,text="Correct!",bg="#29411b",activebackground="#007500",command= justRight)
    right.grid(row=2,column=1)
    right["font"]=TextFont
    right["state"]=DISABLED

    tooHigh= Button(root,width=15,height=5,text="Too High!",bg="#800000",activebackground="#d70000",command= goLower)
    tooHigh.grid(row=2,column=2)
    tooHigh["font"]=TextFont
    tooHigh["state"]=DISABLED

    root.mainloop()