from os import system # importing system from os
from tkinter import * # importing graphic library
import tkinter.messagebox # importing tkinter.messagebox
def Application(self, master=None): # application module
    system('clear') # clean terminal at program starts
root = Tk() # application window
root.title('Triangle') # window title
root.geometry('400x200') # window size
Application(root) # application start
root.mainloop() # call mainloop method
