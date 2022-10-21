# importing system from os
from os import system
# importing graphic library
from tkinter import *
# application module
def Application(self, master=None):
    # reset function
    def Reset():
        # destroy windows
        self.result.destroy()
        # destroy menu
        self.menu.destroy()
        # start
        Start()
    # enter event
    def Enter(event):
        Result()
    # menu module
    def Menu():
        # menu widget
        self.menu = Frame(self.top)
        self.menu.pack(pady=(15, 5))
        # exit button
        exit = Button(self.menu, command=self.top.quit, text='Sair')
        exit.pack(side=LEFT, padx=(2, 2))
        # apply button
        self.apply = Button(self.menu, command=Result, text='Calcular')
        self.apply.pack(side=LEFT, padx=(2, 2))
    # starting window
    def Start():
        # starting window widget
        self.starting = Frame(self.top)
        self.starting.pack()
        # call to action
        self.cta = Label(self.starting, height=3, font=('', 13), text='Ensira o preço do produto\nque deseja calcular o desconto.')
        self.cta.pack(pady=(5, 5))
        # user input widget
        self.userInput = Frame(self.starting)
        self.userInput.pack(pady=(5, 5))
        # user input # price # label
        self.priceLabel = Label(self.userInput, text='R$')
        self.priceLabel.pack(side=LEFT)
        # user input # price
        self.price = Entry(self.userInput, width=12)
        self.price.insert(END, 27.85)
        self.price.bind('<Return>', Enter)
        self.price.pack(side=LEFT)
        # create menu
        Menu()
    # result window
    def Result():
        # get user input price
        input = self.price.get()
        # check if user input have comma if true replace to '.'
        if input.find(',') != -1:
            price = input.replace(',', '.')
        else:
            price = input
        # destroy starting window and menu
        self.starting.destroy()
        self.menu.destroy()
        # result widget
        self.result = Frame(self.top)
        self.result.pack(pady=(45, 35))
        try:
            price = float(price)
            # old price
            # widget
            self.old = Frame(self.result)
            self.old.pack()
            # label
            oldPriceLabel = Label(self.old, text='O produto custava R$')
            oldPriceLabel.pack(side=LEFT)
            # price
            oldPrice = Label(self.old, fg='orange', text='{:.2f}'.format(price))
            oldPrice.pack(side=LEFT)
            # discount
            # widget
            self.new = Frame(self.result)
            self.new.pack()
            # label
            discountLabel = Label(self.new, text='Com 5% de desconto custará R$')
            discountLabel.pack(side=LEFT)
            # price
            newPrice = Label(self.new, fg='green', text='{:.2f}'.format(price * 95 / 100))
            newPrice.pack(side=LEFT)
        except ValueError:
            error = Label(self.result, height=1, fg='red', font=('', 15, 'bold'), text='Erro: USB 01')
            error.pack(pady=(5, 5))
        # create menu
        Menu()
        self.apply['command'] = Reset
        self.apply['text'] = 'Voltar'
    # clean terminal at application starts
    system('clear')
    # top frame
    self.top = Frame(master)
    self.top.pack()
    # create starting window
    Start()
# application setup
root = Tk()
root.title('Discount')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
