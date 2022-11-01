# importing system from os
from os import system
# importing choice from random
from random import choice
# importing graphic library
from tkinter import *
# application module
def Application(self, master=None):
    system('clear') # clean terminal at program starts
# application setup
root = Tk()
root.title('Random')
root.geometry('400x200')
# applicaton start
Application(root)
# mainloop
root.mainloop()
