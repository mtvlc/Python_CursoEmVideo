from os import system # importing system from os
from tkinter import * # importing graphic library
import tkinter.messagebox # importing tkinter.messagebox
def Application(self, master=None): # application module
    system('clear') # clean terminal at program starts
root = Tk() # tkinter window
root.title('<&>') # window title
root.geometry('400x200') # window size
Application(root) # start application
root.mainloop() # call mainloop method
