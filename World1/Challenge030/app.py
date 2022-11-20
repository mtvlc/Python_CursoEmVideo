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
        Check() # call check function
    # checking function
    def Check():
        try:
            # get user input number
            self.number = int(self.userInput.get())
            if self.number % 2 == 0:
                tkinter.messagebox.showinfo('Even', 'O número {} é par.'.format(self.number))
            else:
                tkinter.messagebox.showinfo('Odd', 'O número {} é ímpar.'.format(self.number))
        except ValueError:
            tkinter.messagebox.showerror('Error', 'Erro: USB 01\nInsira um número inteiro')
    system('clear') # clean terminal at program starts
    # top frame
    self.top = Frame(master)
    # call to action
    self.cta = Label(self.top, height=3, font=('', 12, 'bold'), text='Insira um número para verificar\nse o mesmo é par ou ímpar.')
    self.cta.pack(pady=(10, 5))
    # user input
    self.userInput = Entry(self.top, width=6)
    self.userInput.insert(END, 7)
    self.userInput.bind('<Return>', Enter)
    self.userInput.pack(pady=(5, 15))
    # menu widget
    self.menu = Frame(self.top)
    # exit button
    self.exit = Button(self.menu, command=self.top.quit, text='Sair')
    self.exit.pack(side=LEFT, padx=(0, 2))
    # apply button
    self.apply = Button(self.menu, command=Check, text='Verificar')
    self.apply.pack(side=LEFT, padx=(2, 0))
    self.menu.pack(pady=(5, 5))
    self.top.pack()
# application setup
root = Tk()
root.title('Odd|Even')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
