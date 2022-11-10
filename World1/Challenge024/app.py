# importing system from os
from os import system
# importing graphic library
from tkinter import *
# importing tkinter.messagebox
import tkinter.messagebox
# application module
def Application(self, master=None):
    # enter function event # call result function
    def Enter(event):
        Result()
    # result function
    def Result():
        # define user input city name to city variable
        self.city = self.cityInput.get().strip().split()
        # result
        if self.city[0].upper() != 'SANTO':
            tkinter.messagebox.showinfo('Result', 'O nome da cidade "{}" não começa com SANTO.'.format(' '.join(self.city)))
        else:
            tkinter.messagebox.showinfo('Result', 'O nome da cidade "{}" começa com SANTO.'.format(' '.join(self.city)))
    system('clear') # clean terminal at program starts
    # top frame
    self.top = Frame(master)
    # call to action
    self.cta = Label(self.top, height=3, font=('', 12, 'bold'), text='Ensira o nome de uma cidade abaixo\npara ver se o nome começa com SANTO.')
    self.cta.pack(pady=(10, 0))
    # user input
    self.cityInput = Entry(self.top, width=18)
    self.cityInput.insert(END, 'Cidade')
    self.cityInput.bind('<Return>', Enter)
    self.cityInput.pack(pady=(15, 25))
    # menu widget
    self.menu = Frame(self.top)
    # exit button
    self.exit = Button(self.menu, command=self.top.quit, text='Sair')
    self.exit.pack(side=LEFT, padx=(0, 2))
    # apply button
    self.apply = Button(self.menu, command=Result, text='Avaliar')
    self.apply.pack(side=LEFT, padx=(2, 0))
    self.menu.pack()
    self.top.pack()
# application setup
root = Tk()
root.title('NameCity')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
