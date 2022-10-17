# importing requests
import requests
# importing json
import json
# importing system from os
from os import system
# importing graphic library
from tkinter import *
# application module
def Application(self, master=None):
    # reset function
    def Reset():
        self.result.destroy()
        self.menu.destroy()
        Start()
    # get price function
    def GetPrice():
        # connect api
        api = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
        result = api.json()
        self.price = result['USD']['bid']
    # enter event
    def Enter(event):
        Apply()
    # apply function
    def Apply():
        # result widget
        self.result = Frame(self.top)
        self.result.pack()
        # result label
        rLabel = Label(self.result, height=4, font=('', 12), text='')
        try:
            valueInput = float(self.amount.get())
            rLabel['text'] = 'Com R${:.2f} você pode\ncomprar US${:.2f}.'.format(valueInput, valueInput / float(self.price))
            rLabel['font'] = ('', 12, 'bold')
        except ValueError:
            rLabel['text'] = 'Erro: USB 01'
            rLabel['fg'] = 'red'
            rLabel['font'] = ('', 15, 'bold')
        rLabel.pack(pady=(25, 25))
        self.starting.destroy()
        self.menu.destroy()
        Menu()
        self.apply['command'] = Reset
        self.apply['text'] = 'Voltar'
    # menu module
    def Menu():
        # menu widget
        self.menu = Frame(self.top)
        self.menu.pack()
        # exit button
        exit = Button(self.menu, command=self.top.quit, text='Sair')
        exit.pack(side=LEFT, pady=(10, 5), padx=(2, 2))
        # apply button
        self.apply = Button(self.menu, command=Apply, text='Converter')
        self.apply.pack(side=LEFT, pady=(10, 5), padx=(2, 2))
    # starting window module
    def Start():
        # start window widget
        self.starting = Frame(self.top)
        self.starting.pack()
        # call to action
        cta = Label(self.starting, font=('', 13), text='Ensira um valor em reais\npara convertê-lo para dólares.')
        cta.pack(pady=(15, 5))
        # price label
        price = Label(self.starting, fg='green', text='US$1.00 = R${:.2f}.'.format(float(self.price)))
        price.pack(pady=(5, 5))
        # user input widget
        self.userInput = Frame(self.starting)
        self.userInput.pack()
        # label
        real = Label(self.userInput, text='R$')
        real.pack(side=LEFT)
        self.amount = Entry(self.userInput, width=12)
        self.amount.insert(END, 100)
        self.amount.pack(side=LEFT, pady=(5, 5))
        self.amount.bind('<Return>', Enter)
        # menu
        Menu()
    # clear terminal
    system('clear')
    # top frame
    self.top = Frame(master)
    self.top.pack()
    # get price
    GetPrice()
    # starting window
    Start()
# application setup
root = Tk()
root.title('Exchange')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
