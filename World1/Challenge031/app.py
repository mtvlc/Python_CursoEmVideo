# importing system from os
from os import system
# importing graphic library
from tkinter import *
# importing tkinter.messagebox
import tkinter.messagebox
# application module
def Application(self, master=None):
    system('clear') # clean terminal at program starts
# application setup
root = Tk()
root.title('TravelPrice')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
