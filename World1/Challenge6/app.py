# importing system from os
from os import system
# importing graphic library
from tkinter import *
# application module
def Application(self, master=None):
    # clear terminal
    system('clear')
    # reset function
    def Reset():
        self.starting.destroy()
        self.resultWidget.destroy()
        self.menu.destroy()
        Start()
    # apply function
    def Apply():
        # try to change user input 'str' to float
        try:
            number = float(self.userInput.get())
            # transform user input 'float' to 'int' if possible
            if float.is_integer(number):
                number = int(number)
            Result()
            self.result.destroy()
            # result widget
            self.result = Frame(self.resultWidget)
            self.result.pack()
            # double
            double = Label(self.result, font=('', 12, 'bold'), text='O dobro de {} é = {}.'.format(number, number * 2))
            double.pack(pady=(30, 5))
            # triple
            triple = Label(self.result, font=('', 12, 'bold'), text='O triplo de {} é = {}.'.format(number, number * 3))
            triple.pack(pady=(5, 5))
            # square root
            sqrt = Label(self.result, font=('', 12, 'bold'), text='A raiz quadrada de {} é = {:.2f}.'.format(number, number ** 0.5))
            sqrt.pack(pady=(5, 30))
        # if not possible convert user input to float
        except ValueError:
            Result()
            self.result['text'] = 'Erro: USB 01'
            self.result['fg'] = 'red'
            self.result['font'] = ('', 15, 'bold')
            self.result.pack(pady=(65, 60))
    # enter event
    def Enter(event):
        Apply()
    # menu module
    def Menu():
        # menu widget
        self.menu = Frame(self.top)
        self.menu.pack()
        # exit button
        exit = Button(self.menu, command=self.top.quit, text='Sair')
        exit.pack(side=LEFT)
        # apply button
        self.apply = Button(self.menu, command=Apply, text='Mostrar')
        self.apply.pack(side=LEFT)
    # starting window module
    def Start():
        # starting window widget
        self.starting = Frame(self.top)
        self.starting.pack()
        # call to action
        cta = Label(self.starting, height=5, font=('', 12, 'bold'), text='Ensira um número abaixo em seguida\n clique em mostrar para calcular\no dobro, triplo e raiz quadrada.')
        cta.pack()
        # user input
        self.userInput = Entry(self.starting, width=10)
        self.userInput.insert(END, 25)
        self.userInput.pack(pady=(0, 25))
        self.userInput.bind('<Return>', Enter)
        Menu()
    # result window
    def Result():
        self.starting.destroy()
        self.menu.destroy()
        # result widget
        self.resultWidget = Frame(self.top)
        self.resultWidget.pack()
        self.result = Label(self.resultWidget, text='')
        Menu()
        self.apply['command'] = Reset
        self.apply['text'] = 'Voltar'
    # top frame
    self.top = Frame(master)
    self.top.pack()
    # start window
    Start()
# application setup
root = Tk()
root.title('TripleDoubleSquareRoot')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
