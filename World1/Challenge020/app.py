# importing system from os
from os import system
# importing shuffle from random
from random import shuffle
# importing graphic library
from tkinter import *
# application module
def Application(self, master=None):
    system('clear') # clean terminal at program starts
# application setup
root = Tk()
root.title('Shuffle')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
