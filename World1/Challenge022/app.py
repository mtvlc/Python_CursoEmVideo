# importing system from os
from os import system
# importing graphic library
from tkinter import *
# importing tkinter messagebox
import tkinter.messagebox
# application module
def Application(self, master=None):
    # enter event
    def Enter(event):
        Count()
    # count function
    def Count():
        # get name
        self.name = self.userInput.get().strip().upper().split()
        if self.name == '':
            tkinter.messagebox.showerror('Erro: USB 01', 'Ensira um nome para poder contar.')
        else:
            tkinter.messagebox.showinfo('Contagem', 'Somente maiúsculas \n{}\nSomente minúsculas \n{}\nTotal de letras \n{}\nLetras primeiro nome \n{}'.format(' '.join(self.name), ' '.join(self.name).lower(), len(''.join(self.name)), len(self.name[0])))
    system('clear') # clean terminal at program starts
    # top frame
    self.top = Frame(master)
    # call to action
    self.cta = Label(self.top, height=3, font=('', 12, 'bold'), text='Ensira seu nome abaixo\npara contar as letras')
    self.cta.pack()
    # user input
    self.userInput = Entry(self.top)
    self.userInput.bind('<Return>', Enter)
    self.userInput.pack(pady=(15, 15))
    # menu widget
    self.menu = Frame(self.top)
    # exit button
    self.exit = Button(self.menu, command=self.top.quit, text='Sair')
    self.exit.pack(side=LEFT, padx=(0, 2))
    # apply button
    self.apply = Button(self.menu, command=Count, text='Contar')
    self.apply.pack(side=LEFT, padx=(2, 0))
    self.menu.pack(pady=(15, 15))
    self.top.pack()
# application setup
root = Tk()
root.title('Name')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
