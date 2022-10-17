# importing system from os
from os import system
# importing graphic library
from tkinter import *
# application module
def Application(self, master=None):
    # reset function
    def Reset():
        self.start.destroy()
        self.result.destroy()
        self.menu.destroy()
        Start()
    # apply function
    def Apply():
        try:
            n1 = float(self.fNum.get())
            n2 = float(self.sNum.get())
            Result()
            if float.is_integer(n1) and float.is_integer(n2):
                self.resultL['text'] = '{} mais {} é = {}.'.format(int(n1), int(n2), int(n1 + n2))
                self.resultL['fg'] = 'green'
                self.resultL.pack(pady=(35, 30))
            else:
                self.resultL['text'] = '{:.2f} mais {:.2f} é = {:.2f}.'.format(n1, n2, n1+n2)
                self.resultL['fg'] = 'green'
                self.resultL.pack(pady=(35, 35))
        except ValueError:
            Result()
            self.resultL['text'] = 'Erro: USB 01'
            self.resultL['fg'] = 'red'
            self.resultL.pack(pady=(35, 30))
    # menu
    def Menu():
        # menu widget
        self.menu = Frame(self.top)
        self.menu.pack()
        # exit button
        exit = Button(self.menu, command=self.top.quit, text='Sair')
        exit.pack(side=LEFT, padx=(0, 5))
        # apply button
        self.apply = Button(self.menu, command=Apply, text='Calcular')
        self.apply.pack(side=LEFT, padx=(5, 0))
    # starting window
    def Start():
        # stating window widget
        self.start = Frame(self.top)
        self.start.pack()
        # call to action
        cta = Label(self.start, height=3, font=('bold', 15), text='Ensira dois números abaixo\nem seguida clique em calcular.')
        cta.pack()
        # user input
        # labels
        uil = Frame(self.start)
        uil.pack()
        # first number label
        fnl = Label(uil, text='Primeiro número')
        fnl.pack(side=LEFT, padx=(0, 10))
        # second number label
        snl = Label(uil, text='Segundo número')
        snl.pack(side=LEFT, padx=(10, 0))
        # user input widget
        userInput = Frame(self.start)
        userInput.pack()
        # first number
        self.fNum = Entry(userInput, width=7)
        self.fNum.pack(side=LEFT, pady=(5, 15), padx=(0, 40))
        # second number
        self.sNum = Entry(userInput, width=7)
        self.sNum.pack(side=LEFT, pady=(5, 15), padx=(40, 0))
        Menu()
    # result window
    def Result():
        self.start.destroy()
        self.menu.destroy()
        # result window gadget
        self.result = Frame(self.top)
        self.result.pack()
        # result label
        self.resultL = Label(self.result, heigh=3, font=('bold', 15), text='')
        Menu()
        self.apply['command'] = Reset
        self.apply['text'] = 'Voltar'
    # terminal clear
    system('clear')
    # top frame
    self.top = Frame(master)
    self.top.pack()
    Start()
# application setup
root = Tk()
root.title('Soma')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
