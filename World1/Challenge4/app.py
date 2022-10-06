# importing system from os
from os import system
# importing graphic library
from tkinter import *
# application module
def Application(self, master=None):
    # reset function
    def Reset():
        self.startWidget.destroy()
        self.result.destroy()
        self.menu.destroy()
        Start()
    # enter button function
    def Enter(event):
        # get user input
        self.text = self.userInput.get('1.0', 'end-1c').strip()
        Result()
    # menu module
    def Menu():
        # menu widget
        self.menu = Frame(self.top)
        self.menu.pack()
        # exit button
        exit = Button(self.menu, command=self.top.quit, text='Sair')
        exit.pack(side=LEFT, padx=(0, 5))
        # apply button
        self.apply = Button(self.menu, command=Result, text='Detalhes')
        self.apply.pack(side=LEFT, padx=(5, 0))
    # starting window module
    def Start():
        # start window widget
        self.startWidget = Frame(self.top)
        self.startWidget.pack()
        # call to action
        cta = Label(self.startWidget, height=3, font=('bold', 15), text='Digite alguma coisa abaixo\nem seguida clique em detalhes.')
        cta.pack()
        self.userInput = Text(self.startWidget, height=6, width= 45)
        self.userInput.insert(END, 'Lorem ipsum dolor sit amet, consectetur \nadipisicing elit, sed do eiusmod tempor \nincididunt ut labore et dolore magna aliqua.')
        self.userInput.pack(pady=(10, 10))
        self.userInput.bind('<Return>', Enter)
        # menu
        Menu()
    # Result window module
    def Result():
        self.startWidget.destroy()
        self.menu.destroy()
        # result widget
        self.result = Frame(self.top)
        self.result.pack()
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
root.title('String Details')
root.geometry('400x250')
# application start
Application(root)
# mainloop
root.mainloop()
