from os import system # importing system from os
from tkinter import * # importing graphic library
import tkinter.messagebox # importing tkinter.messagebox
def Application(self, master=None): # application module
    def Enter(event): # enter event # call result function
        Result()
    def Raise(): # calc raise value
        if self.salary <= 1250.0: # if salary is under 1250 increase 15%
            self.newSalary = self.salary * 115 / 100
        else: # if salary is more than 1250 increase 10%
            self.newSalary = self.salary * 110 / 100
    def Result(): # result function
        try:
            self.salary = float(self.userInput.get()) # get user input
            Raise()
            tkinter.messagebox.showinfo('Result', 'Salário atual: R${:.2f}\nSalário após ajuste: R${:.2f}\nValor do aumento: R${:.2f}'.format(self.salary, self.newSalary, self.newSalary - self.salary))
        except ValueError:
            tkinter.messagebox.showerror('Error', 'Valor do salário não reconhecido.\nTente novamente.')
    system('clear') # clean terminal at program starts
    def Start(): # start application
        self.top = Frame(master) # top frame
        self.cta = Label(self.top, height=3, font=('', 12, 'bold'), text='Insira seu salário abaixo para\ncalcular o valor do aumento.') # call to action
        self.cta.pack(pady=(15, 5))
        self.userInput = Entry(self.top, width=10) # user input
        self.userInput.insert(END, 1200.80)
        self.userInput.bind('<Return>', Enter) # bind return key
        self.userInput.pack(pady=(10, 25))
        self.menu = Frame(self.top) # menu widget
        self.exit = Button(self.menu, command=self.top.quit, text='Sair') # exit button # close program
        self.exit.pack(side=LEFT, padx=(0, 2))
        self.apply = Button(self.menu, command=Result, text='Calcular') # apply button # call result function
        self.apply.pack(side=LEFT, padx=(2, 0))
        self.menu.pack() # end menu widget
        self.top.pack() # end top frame
    Start() # call start function
root = Tk() # tkinter window
root.title('Salary') # window title
root.geometry('400x200') # window size
Application(root) # start application
root.mainloop() # call mainloop method
