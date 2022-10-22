# importing system from os
from os import system
# importing graphic library
from tkinter import *
# application module
def Application(self, master=None):
    # reset function
    def Reset():
        # destroy result window and his elements
        self.result.destroy()
        self.menu.destroy()
        # start
        Start()
    # floating function # get user input and test floating point
    def Floating():
        # get user input
        self.salary = self.input.get()
        # validate user input
        if self.salary.find(',') != -1:
            # replace ',' to '.'
            self.salary = self.salary.replace(',', '.')
    # enter event
    def Enter(event):
        Result()
    # menu module
    def Menu():
        # widget
        self.menu = Frame(self.top)
        self.menu.pack()
        # exit button
        exit = Button(self.menu, command=self.top.quit, text='Sair')
        exit.pack(side=LEFT, padx=(0, 3))
        # apply button
        self.apply = Button(self.menu, command=Result, text='Calcular')
        self.apply.pack(side=LEFT, padx=(3, 0))
    # starting window module
    def Start():
        # widget
        self.starting = Frame(self.top)
        self.starting.pack()
        # call to action
        cta = Label(self.starting, height=3, font=('', 13), text='Ensira seu salário abaixo\npara calcular o aumento.')
        cta.pack()
        # user input
        # widget
        userInput = Frame(self.starting)
        userInput.pack()
        # label
        currency = Label(userInput, text='R$')
        currency.pack(side=LEFT, pady=(15, 25))
        # input
        self.input = Entry(userInput, width=12)
        self.input.insert(END, 2153.87)
        self.input.bind('<Return>', Enter)
        self.input.pack(side=LEFT, pady=(15, 25))
        # create menu
        Menu()
    # result window
    def Result():
        # check floating
        Floating()
        # destroy starting window and his elements
        self.starting.destroy()
        self.menu.destroy()
        # result window widget
        self.result = Frame(self.top)
        self.result.pack()
        # error window
        self.error = Label(self.result, height=4, fg='red', font=('', 15, 'bold'), text='Erro: USB 01')
        try:
            self.salary = float(self.salary)
            # current salary widget
            self.current = Frame(self.result)
            self.current.pack(pady=(15, 5))
            # label
            currentLabel = Label(self.current, text='Salário atual = R$')
            currentLabel.pack(side=LEFT)
            # value
            current = Label(self.current, fg='orange', text=self.salary)
            current.pack(side=LEFT)
            # new salary widget
            self.new = Frame(self.result)
            self.new.pack(pady=(5, 5))
            # label
            newLabel = Label(self.new, text='Novo salário com 15% de acréscimo = R$')
            newLabel.pack()
            # value
            newSalary = Label(self.new, fg='green', text='{:.2f}'.format(self.salary * 115 / 100))
            newSalary.pack()
            # amount increased widget
            self.increased = Frame(self.result)
            self.increased.pack(pady=(5, 15))
            # label
            increasedLabel = Label(self.increased, text='Valor do aumento = R$')
            increasedLabel.pack(side=LEFT)
            # value
            increased = Label(self.increased, fg='green', text='{:.2f}'.format(self.salary * 115 / 100 - self.salary))
            increased.pack(side=LEFT)
        except ValueError:
            self.error.pack(pady=(25, 15))
        # create menu
        Menu()
        # change apply button command and text
        self.apply['command'] = Reset
        self.apply['text'] = 'Voltar'
    # clean terminal at program starts
    system('clear')
    # top Frame
    self.top = Frame(master)
    self.top.pack()
    # create starting window
    Start()
# application setup
root = Tk()
root.title('Salary')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
