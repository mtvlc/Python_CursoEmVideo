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
        Check()
    # check function
    def Check():
        # speed limit
        self.speedLimit = 80
        try:
            # vehicle speed
            self.vehicleSpeed = int(self.userInput.get())
            if self.vehicleSpeed > self.speedLimit:
                tkinter.messagebox.showerror('Result', 'Veículo acima do limite permitido.\nValor da multa R${:.2f}.'.format((self.vehicleSpeed - self.speedLimit) * 7))
            else:
                tkinter.messagebox.showinfo('Result', 'Veículo dentro do limite de velocidade permitida.')
        except ValueError:
            tkinter.messagebox.showerror('Error', 'Erro: USB 01\nInsira um valor válido.')
    system('clear') # clean terminal at program starts
    # top frame
    self.top = Frame(master)
    # call to action
    self.cta = Label(self.top, height=3, font=('', 12, 'bold'), text='Ensira a velocidade do veículo para\ncalcular o valor da multa.')
    self.cta.pack()
    # user input # vehicle speed
    self.userInput = Entry(self.top, width=6)
    self.userInput.insert(END, 80)
    self.userInput.bind('<Return>', Enter)
    self.userInput.pack(pady=(10, 15))
    # menu widget
    self.menu = Frame(self.top)
    # exit button
    self.exit = Button(self.menu, command=self.top.quit, text='Sair')
    self.exit.pack(side=LEFT, padx=(0, 2))
    # apply button
    self.apply = Button(self.menu, command=Check, text='Calcular')
    self.apply.pack(side=LEFT, padx=(2, 0))
    self.menu.pack()
    self.top.pack()
# application setup
root = Tk()
root.title('SpeedLimit')
root.geometry('400x180')
# application start
Application(root)
# mainloop
root.mainloop()
