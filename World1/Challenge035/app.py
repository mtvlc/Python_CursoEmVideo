from os import system # importing system from os
from tkinter import * # importing graphic library
import tkinter.messagebox # importing tkinter.messagebox
def Application(self, master=None): # application module
    def Enter(event): # enter event
        Loop() # call loop function
    def Back(): # back function
        self.numbers.remove(self.numbers[-1])
        self.top.destroy()
        Main()
    def Loop(): # loop function
        try:
            self.number = float(self.userInput.get())
            if self.number.is_integer() == True:
                self.number = int(self.number)
            self.numbers.append(self.number)
            self.top.destroy()
            Main()
        except ValueError:
            tkinter.messagebox.showerror('Error', 'Erro: USB 01\nNúmero não reconhecido.')
    def Main():
        self.top = Frame(master) # top frame
        self.cta = Label(self.top, height=3, font=('', 12, 'bold'), text='Insira o comprimento de três retas abaixo\npara calcular se é possível\nformar um triângulo.') # call to action
        self.cta.pack(pady=(5, 10)) # if true show call to action
        if len(self.numbers) < 3:
            self.numberLabel = Label(self.top, font=('', 8, 'bold'), text='{}ª reta.'.format(len(self.numbers) + 1))
            self.numberLabel.pack()
            self.userInput = Entry(self.top, width=6) # user input number
            self.userInput.bind('<Return>', Enter) # bind return key
            self.userInput.pack(pady=(5, 15))
            self.menu = Frame(self.top) # menu widget
            self.back = Button(self.menu, command=Back, text='Voltar')
            if len(self.numbers) != 0:
                self.back.pack(side=LEFT, padx=(0, 2))
            self.exit = Button(self.menu, command=self.top.quit, text='Sair') # exit button
            self.exit.pack(side=LEFT, padx=(2, 2))
            self.next = Button(self.menu, command=Loop, text='Próximo')
            self.next.pack(side=LEFT, padx=(2, 0))
            self.menu.pack() # end menu widget
            self.top.pack() # end top frame
        else:
            self.numbers.sort()
            if self.numbers[0] + self.numbers[1] > self.numbers[-1]:
                tkinter.messagebox.showinfo('Result', 'É possível formar um triângulo. \b ')
            else:
                tkinter.messagebox.showinfo('Result', 'Não é possível formar um triângulo.')
            self.numbers.clear()
            self.top.destroy()
            Main()
    system('clear') # clean terminal at program starts
    self.numbers = [] # numbers list
    Main()
root = Tk() # tkinter window
root.title('<&>') # window title
root.geometry('400x200') # window size
Application(root) # start application
root.mainloop() # call mainloop method
