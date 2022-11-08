# importing system from os
from os import system
# importing graphic library
from tkinter import *
# importing tkinter messagebox
import tkinter.messagebox
# application module
def Application(self, master=None):
    # reset function
    def Reset():
        self.result.destroy()
        self.menu.destroy()
        Start()
    # error message
    def Error():
        tkinter.messagebox.showerror('Erro: USB 01', 'Ensira um número entre 0 e 9999!')
    # starting window function
    def Start():
        # starting window widget
        self.starting = Frame(self.top)
        # call to action
        self.cta = Label(self.starting, height=3, font=('', 12, 'bold'), text='Ensira um número de 0 a 9999\npara formatalo para o sistema decimal.')
        self.cta.pack(pady=(5, 15))
        # user input widget
        self.userInput = Frame(self.starting)
        # number entry
        self.numberInput = Entry(self.userInput, width=6)
        self.numberInput.insert(END, 1234)
        self.numberInput.bind('<Return>', Enter)
        self.numberInput.pack(side=LEFT, padx=(0, 5))
        self.userInput.pack(pady=(5, 20))
        self.starting.pack()
        Menu()
    # result function
    def Result():
        golden = ['               Unidade:', '   Unidade Dezena:', '  Unidade Centena:', 'Unidade de Milhar:']
        # get number
        self.numberStr = self.numberInput.get().strip()
        self.digits = []
        # result widget
        self.result = Frame(self.top)
        self.i = 0
        try:
            self.number = int(self.numberStr)
            if self.number >= 0 and self.number <= 9999:
                # destroy starting window and menu
                self.starting.destroy()
                self.menu.destroy()
                for x in self.numberStr:
                    self.digits.append(x)
                self.digits.reverse()
                for x in self.digits: # show results
                    self.digit = Label(self.result, font=('', 10, 'bold'), text='{} {}'.format(golden[self.i], x))
                    self.digit.pack(pady=(5, 5))
                    self.i += 1
                self.result.pack(pady=(10, 5))
                Menu() # call menu
                # set reset function to apply button
                self.apply['command'] = Reset
                self.apply['text'] = 'Voltar'
            else:
                Error()
        except ValueError:
            Error()
    # enter event
    def Enter(event):
        Result()
    # menu function
    def Menu():
        # menu widget
        self.menu = Frame(self.top)
        # exit button
        self.exit = Button(self.menu, command=self.top.quit, text='Sair')
        self.exit.pack(side=LEFT, padx=(0, 2))
        # apply button
        self.apply = Button(self.menu, command=Result, text='Converter')
        self.apply.pack(side=LEFT, padx=(5, 0))
        self.menu.pack()
    system('clear') # clean terminal at program starts
    # top frame
    self.top = Frame(master)
    Start()
    self.top.pack()
# application setup
root = Tk()
root.title('Golden')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
