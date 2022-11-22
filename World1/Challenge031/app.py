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
        Price() # call price function
    # price function
    def Price():
        try:
            # get distance value from user input
            self.distance = float(self.userInput.get())
            if self.distance <= 0:
                tkinter.messagebox.showerror('Error', 'Erro: USB 02\nDistância inválida.  ')
            else:
                if self.distance <= 200:
                    tkinter.messagebox.showinfo('Result', 'Distância da viagem {}km.\nValor da passagem R${:.2f}.'.format(self.distance, self.distance * 0.5))
                else:
                    tkinter.messagebox.showinfo('Result', 'Distância da viagem {}km.\nValor da passagem R${:.2f}.'.format(self.distance, self.distance * 0.45))
        except ValueError:
            tkinter.messagebox.showerror('Error', 'Erro: USB 01\nDistância inválida.  ')
    system('clear') # clean terminal at program starts
    # top frame
    self.top = Frame(master)
    # call to action
    self.cta = Label(self.top, height=3, font=('', 12, 'bold'), text='Insira a distância da viagem abaixo\npara calcular o preço da passagem.')
    self.cta.pack(pady=(15, 5))
    # user input distance
    self.userInput = Entry(self.top, width=8)
    self.userInput.insert(END, 100)
    self.userInput.bind('<Return>', Enter)
    self.userInput.pack(pady=(5, 20))
    # menu widget
    self.menu = Frame(self.top)
    # exit button
    self.exit = Button(self.menu, command=self.top.quit, text='Sair')
    self.exit.pack(side=LEFT, padx=(0, 2))
    # apply button
    self.apply = Button(self.menu, command=Price, text='Calcular')
    self.apply.pack(side=LEFT, padx=(2, 0))
    self.menu.pack()
    self.top.pack()
# application setup
root = Tk()
root.title('TravelPrice')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
