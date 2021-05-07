from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
from random import * 
import random as rand

def outOfRange():
    global keepPlaying
    box = messagebox.askquestion("Error! Out Of Range!","Do You Want To Keep Playing ?",icon="warning")
    if box!="yes":
        keepPlaying=FALSE
    root.destroy()

def goHigher():
    global guess, Min, Max
    Min=guess+1
    try :
        guess=rand.randint(Min,Max)
    except:
        outOfRange()
    compTxt.set(str(guess))

def goLower():
    global guess, Min, Max
    Max=guess-1
    try :
        guess=rand.randint(Min,Max)
    except:
        outOfRange()
    compTxt.set(str(guess))

def justRight():
    global keepPlaying, guess
    box = messagebox.askquestion("Your Number Is "+str(guess),"Do You Want To Keep Playing ?",icon="question")
    if box!="yes":
        keepPlaying=FALSE
    root.destroy()

def ClickedOnce(guess):
    compTxt.set(str(guess))
    tooLow["state"]=NORMAL
    tooHigh["state"]=NORMAL
    right["state"]=NORMAL
    computer["state"]=DISABLED

keepPlaying= TRUE
while keepPlaying== TRUE:    
    root= tk.Tk()
    root.title("flippity flip")
    root.iconbitmap(r'images/camera.ico')
    root.configure(bg="#FAF9FC")
    CompGenFont= font.Font(family="Times",size=20,weight="bold",slant="italic")
    TextFont= font.Font(family="Times",weight="bold")

    global guess, Min, Max 
    Min=0
    Max=1000
    guess=rand.randint(Min,Max)

    #defining the buttons
    compTxt = tk.StringVar()
    computer= Button(root, bd=0, textvariable=compTxt, width=28, height=5, fg="#978DC1", disabledforeground="#978DC1", activeforeground ='#978DC1', bg="#DCD3FE", activebackground="#ECD3FD", command= lambda : ClickedOnce(guess)  )
    computer.grid(pady=2, row=1,column=0,columnspan=3)
    #computer["state"]=DISABLED
    computer["relief"]="sunken"
    compTxt.set("Choose a number in 0-1000 \nClick Me To Generate \nThe First Number")
    computer["font"]=CompGenFont

    tooLow= Button(root,bd=0,width=15,height=5,text="Too Low!",disabledforeground="#387DC1",activeforeground="#387DC1", fg="#387DC1",bg="#DCD3FE",activebackground="#AEE8FE",command= goHigher)
    tooLow.grid(padx=2,pady=2,row=2,column=0)
    tooLow["font"]=TextFont
    tooLow["state"]=DISABLED

    right= Button(root,bd=0,width=18,height=5,text="Correct!",disabledforeground="#5FB58E",activeforeground="#5FB58E",  fg="#5FB58E",bg="#DCD3FE",activebackground="#D9FED3",command= justRight)
    right.grid(padx=2,pady=2,row=2,column=1)
    right["font"]=TextFont
    right["state"]=DISABLED

    tooHigh= Button(root,bd=0,width=15,height=5,text="Too High!",disabledforeground="#B55A5A",activeforeground="#B55A5A", fg="#B55A5A",bg="#DCD3FE",activebackground="#FEC9DD",command= goLower)
    tooHigh.grid(padx=2,pady=2,row=2,column=2)
    tooHigh["font"]=TextFont
    tooHigh["state"]=DISABLED

    root.mainloop()