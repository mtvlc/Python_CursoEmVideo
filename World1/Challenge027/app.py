# importing system from os
from os import system
# importing graphic library
from tkinter import *
# importing tkinter.messagebox module
import tkinter.messagebox
# application module
def Application(self, master=None):
    # enter event
    def Enter(event):
        Format() # call format function
    # format function
    def Format():
        # get name from user input
        self.name = self.ui.get().strip().title().split()
        if len(self.name) == 1:
            tkinter.messagebox.showinfo('Result', 'Primeiro nome: {}.\nÚltimo nome:              '.format(self.name[0]))
        else:
            tkinter.messagebox.showinfo('Result', 'Primeiro nome: {}.\nÚltimo nome: {}.'.format(self.name[0], self.name[-1]))
    system('clear') # clean terminal at program starts
    # top frame
    self.top = Frame(master)
    # call to action
    self.cta = Label(self.top, height=2, font=('', 12, 'bold'), text='Insira seu nome completo abaixo.')
    self.cta.pack(pady=(15, 10))
    # user input
    self.ui = Entry(self.top, width=30)
    self.ui.bind('<Return>', Enter)
    self.ui.pack(pady=(10, 10))
    # menu widget
    self.menu = Frame(self.top)
    # exit button
    self.exit = Button(self.menu, command=self.top.quit, text='Sair')
    self.exit.pack(side=LEFT, padx=(0, 2))
    # apply button
    self.apply = Button(self.menu, command=Format, text='Formatar')
    self.apply.pack(side=LEFT, padx=(2, 0))
    self.menu.pack(pady=(10, 0))
    self.top.pack()
# application setup
root = Tk()
root.title('Naming')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
