# importing system from os
from os import system
# importing graphic library
from tkinter import *
# application module
def Application(self, master=None):
    # menu
    def Menu():
        # menu widget
        self.menu = Frame(self.top)
        self.menu.pack()
        # exit button
        exit = Button(self.menu, command=self.top.quit, text='Sair')
        exit.pack()
    # starting window
    def Start():
        # stating window widget
        self.start = Frame(self.top)
        self.start.pack()
        # call to action
        cta = Label(self.start, height=3, font=('bold', 15), text='Ensira dois números abaixo\nem seguida clique em calcular.')
        cta.pack()
        Menu()
    # terminal clear
    system('clear')
    # top frame
    self.top = Frame(master)
    self.top.pack()
    Start()
# application setup
root = Tk()
root.title('Soma')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
