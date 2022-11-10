# importing system from os
from os import system
# importing graphic library
from tkinter import *
# importing tkinter.messagebox
import tkinter.messagebox
# application module
def Application(self, master=None):
    # result function
    def Result():
        # get name from user input
        self.name = self.nameEntry.get().strip().upper()
        if self.name.find('SILVA') >= 0:
            tkinter.messagebox.showinfo('Result', 'O nome contém "Silva".  \b')
        else:
            tkinter.messagebox.showinfo('Result', 'O nome não contém "Silva".')
    # enter event
    def Enter(event):
        Result() # call result function
    system('clear') # clean terminal at program starts
    # top frame
    self.top = Frame(master)
    # call to action
    self.cta = Label(self.top, height=3, font=('', 12, 'bold'), text='Ensira um nome abaixo para conferir\nse o mesmo contém "Silva".')
    self.cta.pack(pady=(10, 15))
    # user input
    self.nameEntry = Entry(self.top)
    self.nameEntry.insert(END, 'Nome')
    self.nameEntry.bind('<Return>', Enter)
    self.nameEntry.pack(pady=(5, 25))
    # menu widget
    self.menu = Frame(self.top)
    # exit button
    self.exit = Button(self.menu, command=self.top.quit, text='Sair')
    self.exit.pack(side=LEFT, padx=(0, 2))
    # apply button
    self.apply = Button(self.menu, command=Result, text='Verificar')
    self.apply.pack(side=LEFT, padx=(2, 0))
    self.menu.pack()
    self.top.pack()
# application setup
root = Tk()
root.title('SilvaChecker')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
