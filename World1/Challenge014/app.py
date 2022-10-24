# importing system from os
from os import system
# importing graphic library
from tkinter import *
# application module
def Application(self, master=None):
    # wipe function
    def Wipe():
        # blow up windows and menus
        self.starting.destroy()
        self.resultWidget.destroy()
        self.menu.destroy()
        # restart
        Start()
    # enter event
    def Enter(event):
        Result()
    # menu module
    def Menu():
        # menu widget
        self.menu = Frame(self.top)
        self.menu.pack()
        # exit button
        exit = Button(self.menu, command=self.top.quit, text='Sair')
        exit.pack(side=LEFT)
        # apply button
        self.apply = Button(self.menu, command=Result, text='Converter')
        self.apply.pack(side=LEFT)
    # starting window module
    def Start():
        # starting window widget
        self.starting = Frame(self.top)
        self.starting.pack()
        # call to action
        cta = Label(self.starting, height=3, font=('', 13), text='Ensira uma temperatura em º Celsius\npara convertê-la para Fahrenheit.')
        cta.pack()
        # user input widget
        userInput = Frame(self.starting)
        userInput.pack(pady=(15, 25))
        # label
        degreesLabel = Label(userInput, text='ºC')
        degreesLabel.pack(side=LEFT)
        # input
        self.degrees = Entry(userInput, width=5)
        self.degrees.insert(END, 22.5)
        self.degrees.bind('<Return>', Enter)
        self.degrees.pack(side=LEFT)
        # create menu
        Menu()
    # result window module
    def Result():
        # result widget
        self.resultWidget = Frame(self.top)
        self.resultWidget.pack()
        try:
            # get float number from user input
            degrees = float(self.degrees.get())
            # destroy starting window and menu
            self.starting.destroy()
            self.menu.destroy()
            # convert Celsius to Fahrenheit
            if degrees == 1:
                fahrenheit = Label(self.resultWidget, height=4, font=('', 15), text='{:.1f}ºC equivale a {:.1f}ºF.'.format(degrees, degrees * 1.800 + 32.00))
            else:
                fahrenheit = Label(self.resultWidget, height=4, font=('', 15), text='{:.1f}ºC equivalem a {:.1f}ºF.'.format(degrees, degrees * 1.800 + 32.00))
            fahrenheit.pack(pady=(25, 10))
        except ValueError:
            # destroy starting window and menu
            self.starting.destroy()
            self.menu.destroy()
            # error massage
            error = Label(self.resultWidget, fg='red', height=4, font=('', 15, 'bold'), text='Erro: USB 01')
            error.pack(pady=(25, 10))
        # create menu
        Menu()
        # edit apply button to wipe function
        self.apply['command'] = Wipe
        self.apply['text'] = 'Voltar'
    # clean terminal at program starts
    system('clear')
    # top frame
    self.top = Frame(master)
    self.top.pack()
    # create starting window
    Start()
# application setup
root = Tk()
root.title('Celsius<to>Fahrenheit')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
