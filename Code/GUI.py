import os
import random
from tkinter import *
from PIL import ImageTk, Image
import time
from tkinter import messagebox




def CreateGui():
    
    
    def RunForwardChecking():
        if messagebox.askokcancel("Quit", "Are you sure you want to start the ForwardChecking?"):
            start_input.destroy()
            os.system("D:\co\Summer\CS340\Project\Code\ForwardChecking.py")
        else:
            start_input.destroy()
            os.system("D:\co\Summer\CS340\Project\Code\GUI.py")


    def RunArcConsistency():
        if messagebox.askokcancel("Quit", "Are you sure you want to start the ArcConsistency?"):
            start_input.destroy()
            os.system("D:\co\Summer\CS340\Project\Code\ArcConsistency.py")
        else:
            start_input.destroy()
            os.system("D:\co\Summer\CS340\Project\Code\GUI.py")
            

    def RunBackTracking():
        if messagebox.askokcancel("Quit", "Are you sure you want to start the BackTracking?"):
            start_input.destroy()
            os.system("D:\co\Summer\CS340\Project\Code\Backtracking.py")
        else:
            start_input.destroy()
            os.system("D:\co\Summer\CS340\Project\Code\GUI.py")   

    start_input = Tk()
    
    start_input.title("Car Parking Lot")
    start_input.iconbitmap(default="D:\co\Summer\CS340\Project\images\parking_sign.ico")
    start_input.attributes("-topmost", True) 
    start_input.geometry('500x300+650+400')

    Label(start_input, text="Choose Which Algorthim to run:",anchor= NW , font=("Arial" , 10)).place(x=150,y=50)
    Button(start_input, text = 'ForwadChecking', command=RunForwardChecking ,anchor= NW).place(x=97,y=100)
    Button(start_input, text = 'Arc Consistancy', command= RunArcConsistency ,anchor= NW).place(x=200,y=100)
    Button(start_input, text = 'BackTracking', command= RunBackTracking ,anchor= NW).place(x=300,y=100)

    start_input.mainloop()
    
CreateGui()