# importing system from os
from os import system
# importing graphic library
from tkinter import *
# application module
def Application(self, master=None):
    # reset function
    def Reset():
        # destroy window and menu
        self.result.destroy()
        self.menu.destroy()
        Start() # restart app
    # hypotenuse function
    def Hypotenuse():
        opposite = float(self.opposite.get())
        adjacent = float(self.adjacent.get())
        self.resultLabel['text'] = 'O valor da hipotenusa é = {:.2f}.'.format(pow(pow(opposite, 2) + pow(adjacent, 2), 0.5))
        self.resultLabel['font'] = ('', 12)
    # menu module
    def Menu():
        # menu widget
        self.menu = Frame(self.top)
        self.menu.pack()
        # exit button
        exit = Button(self.menu, command=self.top.quit, text='Sair')
        exit.pack(side=LEFT, padx=(0, 2))
        # apply button
        self.apply = Button(self.menu, command=Result, text='Calcular')
        self.apply.pack(side=LEFT, padx=(2, 0))
    # startig window module
    def Start():
        # starting window widget
        self.starting = Frame(self.top)
        self.starting.pack()
        # call to action
        cta = Label(self.starting, height=3, font=('', 12), text='Ensira o cateto oposto e o cateto adjacente\npara calcular a hipotenusa.')
        cta.pack()
        # user input widget
        userInput = Frame(self.starting)
        # opposite cathet widget
        opposite = Frame(userInput)
        opposite.pack(pady=(2, 2))
        # label
        oppositeLabel = Label(opposite, text='Cateto oposto')
        oppositeLabel.pack(side=LEFT)
        # value # entry
        self.opposite = Entry(opposite, width=6)
        self.opposite.insert(END, 22.7)
        self.opposite.pack(side=LEFT, padx=(20, 0))
        # adjacent cathet widget
        adjacent = Frame(userInput)
        adjacent.pack(pady=(2, 2))
        # label
        adjacentLabel = Label(adjacent, text='Cateto adjacente')
        adjacentLabel.pack(side=LEFT)
        # value # entry
        self.adjacent = Entry(adjacent, width=6)
        self.adjacent.insert(END, 18.25)
        self.adjacent.pack(side=LEFT)
        userInput.pack(pady=(5 ,10))
        Menu() # create menu
    # result window module
    def Result():
        # result window widget
        self.result = Frame(self.top)
        self.result.pack()
        self.resultLabel = Label(self.result, height=6, text='')
        try:
            Hypotenuse()
        except ValueError: # show error code
            self.resultLabel['text'] = 'Erro: USB 01'
            self.resultLabel['fg'] = 'red'
            self.resultLabel['font'] = ('', 13, 'bold')
        # destroy menu and starting window
        self.starting.destroy()
        self.menu.destroy()
        self.resultLabel.pack()
        Menu() # create menu
        # set apply button to reset function
        self.apply['command'] = Reset
        self.apply['text'] = 'Voltar'
    # clean terminal at program starts
    system('clear')
    # top frame
    self.top = Frame(master)
    self.top.pack()
    Start() # create starting window
# application setup
root = Tk()
root.title('Hypotenuse')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
