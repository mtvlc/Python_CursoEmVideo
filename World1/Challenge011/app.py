# importing system from os
from os import system
# importing graphic library
from tkinter import *
# application module
def Application(self, master=None):
    # clear terminal
    system('clear')
# application setup
root = Tk()
root.title('Painter')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
