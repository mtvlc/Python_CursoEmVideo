# importing truncate from math
from math import trunc
# importing system from os
from os import system
# importing graphic library
from tkinter import *
# application module
def Application(self, master=None):
    # reset function
    def Reset():
        # destroy window and menu
        self.result.destroy()
        self.menu.destroy()
        Start() # restart program
    # enter event
    def Enter(event):
        Result()
    # menu module
    def Menu():
        # menu widget
        self.menu = Frame(self.top)
        self.menu.pack()
        # exit button
        exit = Button(self.menu, command=self.top.quit, text='Sair')
        exit.pack(side=LEFT, padx=(0, 2))
        # apply button
        self.apply = Button(self.menu, command=Result, text='Mostrar')
        self.apply.pack(side=LEFT, padx=(2, 0))
    # staring window module
    def Start():
        # starting window widget
        self.starting = Frame(self.top)
        self.starting.pack()
        # call to action
        cta = Label(self.starting, height=3, font=('', 12), text='Ensira um número abaixo\npara mostrar sua parte inteira.')
        cta.pack()
        # user input
        self.number = Entry(self.starting, width=10)
        self.number.insert(END, 3.14)
        self.number.bind('<Return>', Enter)
        self.number.pack(pady=(5 ,5))
        # hint
        hint = Label(self.starting, font=('', 8), text='Para números Reais usar . invés de ,')
        hint.pack(pady=(5, 10))
        Menu() # create menu widget
    # result window module
    def Result():
        # result widget
        self.result = Frame(self.top)
        self.result.pack()
        result = Label(self.result, height=6, font=('', 12), text='')
        try: # get user input number and show result
            number = float(self.number.get())
            result['text'] = 'A parte inteira do número {}\n é {}.'.format(number, trunc(number))
        except ValueError: # show error
            result['text'] = 'Erro: USB 01'
            result['font'] = ('', 12, 'bold')
            result['fg'] = 'red'
        # destroy starting window and menu
        self.starting.destroy()
        self.menu.destroy()
        result.pack() # show result label
        Menu() # create menu widget
        self.apply['command'] = Reset
        self.apply['text'] = 'Voltar'
    # clean terminal at program starts
    system('clear')
    # top frame
    self.top = Frame(master)
    self.top.pack()
    Start() # create starting window
# application setup
root = Tk()
root.title('Truncate')
root.geometry('400x180')
# application start
Application(root)
# mainloop
root.mainloop()
