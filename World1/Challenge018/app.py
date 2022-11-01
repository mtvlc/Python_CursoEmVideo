# importing radians, sin, cos, tan from math
from math import radians, sin, cos, tan
# importing system from os
from os import system
# importing graphic library
from tkinter import *
# application module
def Application(self, master=None):
    # clean terminal at program starts
    system('clear')
# applicaton setup
root = Tk()
root.title('Sin,Cos,Tan')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
