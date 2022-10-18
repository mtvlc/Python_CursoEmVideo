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
    # menu module
    def Menu():
        # menu widget
        self.menu = Frame(self.top)
        self.menu.pack()
        # exit button
        exit = Button(self.menu, command=self.top.quit, text='Sair')
        exit.pack(side=LEFT, pady=(10, 5), padx=(2, 2))
        # apply button
        self.apply = Button(self.menu, command=Result, text='Calcular')
        self.apply.pack(side=LEFT, pady=(10,5), padx=(2, 2))
    # starting window module
    def Start():
        # starting window widget
        self.starting = Frame(self.top)
        self.starting.pack()
        # call to action
        cta = Label(self.starting, font=('', 12), text='Ensira as dimensões da parade abaixo para\ncalcular a quantidade necessária de tinta\npara pintá-la.')
        cta.pack(pady=(10, 5))
        # user input widget
        self.userInputH = Frame(self.starting)
        self.userInputH.pack()
        self.userInputW = Frame(self.starting)
        self.userInputW.pack()
        # height
        heightLabel = Label(self.userInputH, text='Altura')
        self.height = Entry(self.userInputH, width=7)
        self.height.insert(END, 2.50)
        heightLabel.pack(side=LEFT)
        self.height.pack(padx=(10, 0), pady=(2, 2))
        # width
        widthLabel = Label(self.userInputW, text='Largura')
        self.width = Entry(self.userInputW, width=7)
        self.width.insert(END, 3)
        widthLabel.pack(side=LEFT)
        self.width.pack(pady=(2, 2))
        # menu
        Menu()
    # result window module
    def Result():
        # result window widget
        self.result = Frame(self.top)
        self.result.pack()
        self.resultLabel = Label(self.result, height=6, font=('', 13, 'bold'), text='')
        try:
            height = float(self.height.get())
            width = float(self.width.get())
            area = height * width
            # destroy stating window
            self.starting.destroy()
            self.menu.destroy()
            # result
            self.resultLabel['text'] = 'Para uma área de {:.2f}m²\nvocê precisára de {:.2f}l de tinta.'.format(area, area / 2)
            self.resultLabel['fg'] = 'orange'
        except ValueError:
            self.starting.destroy()
            self.menu.destroy()
            self.resultLabel['text'] = 'Erro: USB 01'
            self.resultLabel['fg'] = 'red'
        self.resultLabel.pack()
        # Menu
        Menu()
        self.apply['command'] = Reset
        self.apply['text'] = 'Voltar'
    # clear terminal
    system('clear')
    # top frame
    self.top = Frame(master)
    self.top.pack()
    # starting window
    Start()
# application setup
root = Tk()
root.title('Painter')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
