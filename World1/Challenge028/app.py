# importing system from os
from os import system
# importing randint from random
from random import randint
# importing graphic library
from tkinter import *
# importing tkinter.messagebox
import tkinter.messagebox
# application module
def Application(self, master=None):
    # random function
    def Random():
        # computer choice
        self.cc = randint(0, 5)
        # attempts
        self.attempts = 0
    # zero function
    def Zero():
        self.userChoice = 0
        Check()
    # one
    def One():
        self.userChoice = 1
        Check()
    # two
    def Two():
        self.userChoice = 2
        Check()
    # three
    def Three():
        self.userChoice = 3
        Check()
    # four
    def Four():
        self.userChoice = 4
        Check()
    # five
    def Five():
        self.userChoice = 5
        Check()
    def Check():
        if self.userChoice == self.cc:
            if self.attempts == 0:
                tkinter.messagebox.showinfo('Perfect!', 'Perfeito! Você acertou o número na primeira tentativa.')
            else:
                tkinter.messagebox.showinfo('Win', 'Você acertou! \b\nNúmero de tentativas {}.'.format(self.attempts))
            Random()
        else:
            self.attempts += 1
            tkinter.messagebox.showerror('Error', 'Errou! não escolhi esse número.\nTente novamente.')
    # choose a random number between 0 to 5
    Random()
    system('clear') # clean terminal at program starts
    # top frame
    self.top = Frame(master)
    # call to action
    self.cta = Label(self.top, height=2, font=('', 12, 'bold'), text='Eu escolhi um número entre 0 e 5 tente\nadivinhar qual número eu escolhi.')
    self.cta.pack(pady=(10, 5))
    # numbers widget
    self.numbers = Frame(self.top)
    # zero
    self.numberZero = Button(self.numbers, command=Zero, text='0')
    self.numberZero.pack(side=LEFT, padx=(0, 5))
    # one
    self.numberOne = Button(self.numbers, command=One, text='1')
    self.numberOne.pack(side=LEFT, padx=(5, 5))
    # two
    self.numberTwo = Button(self.numbers, command=Two, text='2')
    self.numberTwo.pack(side=LEFT, padx=(5, 0))
    self.numbers.pack(pady=(10, 5))
    self.numbersTwo = Frame(self.top)
    # three
    self.numberThree = Button(self.numbersTwo, command=Three, text='3')
    self.numberThree.pack(side=LEFT, padx=(0, 5))
    # four
    self.numberFour = Button(self.numbersTwo, command=Four, text='4')
    self.numberFour.pack(side=LEFT, padx=(5, 5))
    # five
    self.numberFive = Button(self.numbersTwo, command=Five, text='5')
    self.numberFive.pack(side=LEFT, padx=(5, 0))
    self.numbersTwo.pack(pady=(5, 10))
    # menu
    self.menu = Frame(self.top)
    # exit button
    self.exit = Button(self.menu, command=self.top.quit, text='Sair')
    self.exit.pack(side=LEFT, padx=(0, 2))
    self.menu.pack()
    self.top.pack()
# application setup
root = Tk()
root.title('Random')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
