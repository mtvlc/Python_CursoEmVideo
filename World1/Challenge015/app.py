# importing system from os
from os import system
# importing graphic library
from tkinter import *
# application module
def Application(self, maste=None):
    # clear terminal at program starts
    system('clear')
# application setup
root = Tk()
root.title('CarRent')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
