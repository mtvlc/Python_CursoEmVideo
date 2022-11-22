# importing system from os
from os import system
# importing graphic library
from tkinter import *
# importing tkinter.messagebox
import tkinter.messagebox
# importing datetime from datetime
from datetime import datetime
# application module
def Application(self, master=None):
    # enter event
    def Enter(event):
        Calc() # call calc function
    # leap function
    def Leap():
        try:
            # get user input
            self.year = int(self.userInput.get())
            # checking if user input year is a leap year
            if self.year % 4 == 0:
                if self.year % 100 != 0:
                    self.leap = True
                else:
                    self.leap = False
            elif self.year % 400 == 0:
                self.leap = True
            else:
                self.leap = False
        except ValueError:
            tkinter.messagebox.showerror('Error', 'Erro: USB 01\nAno inválido.')
    # result function
    def Result():
        # current year
        self.currentYear = datetime.now().year
        if self.year != self.currentYear:
            if self.year > self.currentYear:
                if self.leap == True:
                    tkinter.messagebox.showinfo('Result', '{} será um ano bissexto. \b '.format(self.year))
                else:
                    tkinter.messagebox.showinfo('Result', '{} não será um ano bissexto.'.format(self.year))
            else:
                if self.leap == True:
                    tkinter.messagebox.showinfo('Result', '{} foi um ano bissexto. \b '.format(self.year))
                else:
                    tkinter.messagebox.showinfo('Result', '{} não foi um ano bissexto.'.format(self.year))
        else:
            if self.leap == True:
                tkinter.messagebox.showinfo('Result', '{} é um ano bissexto. \b'.format(self.year))
            else:
                tkinter.messagebox.showinfo('Result', '{} não é um ano bissexto.'.format(self.year))
    # calc function
    def Calc():
        Leap()
        Result()
    system('clear') # clean terminal at program starts
    # top frame
    self.top = Frame(master)
    # call to action
    self.cta = Label(self.top, height=3, font=('', 12, 'bold'), text='Insira um ano abaixo para calcular\nse ele é ou não bissexto.')
    self.cta.pack(pady=(10, 5))
    # user input year
    self.userInput = Entry(self.top, width=6)
    self.userInput.insert(END, 1996)
    self.userInput.bind('<Return>', Enter)
    self.userInput.pack(pady=(5, 15))
    # menu widget
    self.menu = Frame(self.top)
    # apply button
    self.apply = Button(self.menu, command=Calc, text='Calcular')
    self.apply.pack(pady=(0, 2))
    # exit button
    self.exit = Button(self.menu, command=self.top.quit, text='Sair')
    self.exit.pack(pady=(2, 0))
    self.menu.pack()
    self.top.pack()
# application setup
root = Tk()
root.title('LeapYear')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
