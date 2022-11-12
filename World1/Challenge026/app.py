# importing system from os
from os import system
# importing graphic library
from tkinter import *
# importing tkinter.messagebox
import tkinter.messagebox
# application module
def Application(self, master=None):
    # enter event
    def Enter(event):
        Result() # call result function
    # result function
    def Result():
        # get user input
        self.phrase = self.ui.get('1.0', 'end')
        # count
        self.count = self.phrase.upper().count('A')
        # first index
        self.first = self.phrase.upper().find('A')
        # last index
        self.last = self.phrase.upper().rfind('A')
        if self.count == 0 or self.count == 1:
            if self.count == 0:
                tkinter.messagebox.showinfo('Result', 'A letra "A" não aparece nenhuma vez no texto.')
            else:
                tkinter.messagebox.showinfo('Result', 'A letra "A" aparece 1 vez no texto ela aparece na posição {}.'.format(self.first + 1))
        else:
            tkinter.messagebox.showinfo('Result', 'A letra "A" aparace {} vezes no texto. Ela aparece pela 1ª vez na {} posição e pela última vez na posição {}.'.format(self.count, self.first + 1, self.last + 1))
    system('clear') # clean terminal at program starts
    # top frame
    self.top = Frame(master)
    # call to action
    self.cta = Label(self.top, height=3, font=('', 12, 'bold'), text='Insira um texto para análise\nno campo abaixo.')
    self.cta.pack()
    # user input
    self.ui = Text(self.top, height=5, width=40)
    self.ui.bind('<Return>', Enter)
    self.ui.pack()
    # menu widget
    self.menu = Frame(self.top)
    # exit button
    self.exit = Button(self.menu, command=self.top.quit, text='Sair')
    self.exit.pack(side=LEFT, padx=(0, 2))
    # apply button
    self.apply = Button(self.menu, command=Result, text='Analisar')
    self.apply.pack(side=LEFT, padx=(2, 0))
    self.menu.pack()
    self.top.pack()
# application setup
root = Tk()
root.title('LetterA')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
