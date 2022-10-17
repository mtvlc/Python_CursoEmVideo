# importing system from os
from os import system
# importing graphic library
from tkinter import *
# application module
def Application(self, master=None):
    # reset function
    def Reset():
        self.result.destroy()
        self.apply['command'] = Result
        self.reset.pack_forget()
    # menu module
    def Menu():
        # menu widget
        self.menu = Frame(self.top)
        self.menu.pack(pady=(0, 5))
        # exit button
        exit = Button(self.menu, command=self.top.quit, text='Sair')
        exit.pack(side=LEFT)
        # apply button
        self.apply = Button(self.menu, command=Result, text='Calcular')
        self.apply.pack(side=LEFT)
        # reset button
        self.reset = Button(self.menu, command=Reset, text='Voltar')
    # starting window
    def Start():
        # starting window widget
        self.starting = Frame(self.top)
        self.starting.pack()
        # call to action
        cta = Label(self.starting, font=('', 15), text='Ensira um número abaixo em seguida\nclique em calcular para ver a tabuada\ndo número inserido.')
        cta.pack(pady=(5, 5))
        # user input
        self.input = Entry(self.starting, width=15)
        self.input.insert(END, 10)
        self.input.pack(pady=(5, 10))
        Menu()
    # result function
    def Result():
        self.result = Frame(self.top)
        self.result.pack()
        try:
            number = int(self.input.get())
            x = 0
            self.apply['command'] = ''
            # result widget
            while x <= 10:
                self.n = Label(self.result, fg='orange', font=('', 10, 'bold'), text='{:2d} x {:2d} = {:2d}'.format(number, x, number * x))
                self.n.pack()
                x += 1
            self.reset.pack()
        except ValueError:
            error = Label(self.result, fg='red', font=('', 15, 'bold'), text='Erro: USB 01')
            error.pack()
            self.apply['command'] = ''
            self.reset.pack()
    # terminal clear
    system('clear')
    # top frame
    self.top = Frame(master)
    self.top.pack()
    # start window
    Start()
# application setup
root = Tk()
root.title('Multiplication')
root.geometry('400x400')
# application start
Application(root)
# mainloop
root.mainloop()
