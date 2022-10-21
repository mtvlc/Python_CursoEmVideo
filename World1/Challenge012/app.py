# importing system from os
from os import system
# importing graphic library
from tkinter import *
# application module
def Application(self, master=None):
    # enter event
    def Enter(event):
        Result()
    # menu module
    def Menu():
        # menu widget
        self.menu = Frame(self.top)
        self.menu.pack(pady=(15, 5))
        # exit button
        exit = Button(self.menu, command=self.top.quit, text='Sair')
        exit.pack(side=LEFT, padx=(2, 2))
        # apply button
        self.apply = Button(self.menu, command=Result, text='Calcular')
        self.apply.pack(side=LEFT, padx=(2, 2))
    # starting window
    def Start():
        # starting window widget
        self.starting = Frame(self.top)
        self.starting.pack()
        # call to action
        self.cta = Label(self.starting, height=3, font=('', 13), text='Ensira o preço do produto\nque deseja calcular o desconto.')
        self.cta.pack(pady=(5, 5))
        # user input widget
        self.userInput = Frame(self.starting)
        self.userInput.pack(pady=(5, 5))
        # user input # price
        self.priceLabel = Label(self.userInput, text='R$')
        self.priceLabel.pack(side=LEFT)
        self.price = Entry(self.userInput, width=12)
        self.price.insert(END, 27.85)
        self.price.bind('<Return>', Enter)
        self.price.pack(side=LEFT)
        # create menu
        Menu()
    # result window
    def Result():
        pass
    # clean terminal at application starts
    system('clear')
    # top frame
    self.top = Frame(master)
    self.top.pack()
    # create starting window
    Start()
# application setup
root = Tk()
root.title('Discount')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
