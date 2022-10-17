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
        self.result.destroy()
        self.menu.destroy()
        Start()
    # Enter function
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
        self.apply.pack()
    # starting window module
    def Start():
        # starting window widget
        self.starting = Frame(self.top)
        self.starting.pack()
        # call to action
        cta = Label(self.starting, height=4, font=('', 12, 'bold'), text='Ensira um número abaixo\nem seguida clique em MOSTRAR.')
        cta.pack()
        # user input
        self.input = Entry(self.starting, width=15)
        self.input.insert(END, 0)
        self.input.pack(pady=(20, 25))
        self.input.bind('<Return>', Enter)
        # menu
        Menu()
    # result window
    def Result():
        self.starting.destroy()
        self.menu.destroy()
        # result window widget
        self.result = Frame(self.top)
        self.result.pack()
        # user input number widget
        self.uin = Frame(self.result)
        # user input text
        self.uit = Label(self.uin, font=('', 10), text='Você enseriu o número: ')
        self.uit.pack(side=TOP, pady=(10, 2))
        # user input number
        self.uiNum = Label(self.uin, fg='#ff7400', font=('', 10, 'bold'), text='{}'.format(self.number))
        self.uiNum.pack(side=BOTTOM, pady=(2, 2))
        # predecessor number widget
        self.prenum = Frame(self.result)
        # label
        self.prelabel = Label(self.prenum, font=('', 10), text='Número antecessor: ')
        self.prelabel.pack(side=TOP, pady=(2, 2))
        # number
        predecessor = Label(self.prenum, fg='#ff7400', font=('', 10, 'bold'), text='{}'.format(self.number - 1))
        predecessor.pack(side=BOTTOM, pady=(2, 2))
        # successor number widget
        self.nextn = Frame(self.result)
        # label
        nextlabel = Label(self.nextn, font=('', 10), text='Número sucessor: ')
        nextlabel.pack(side=TOP, pady=(2, 2))
        # number
        nextnumber = Label(self.nextn, fg='#ff7400', font=('', 10, 'bold'), text='{}'.format(self.number + 1))
        nextnumber.pack(side=BOTTOM, pady=(2, 2))
        # menu
        Menu()
        self.apply['command'] = Reset
        self.apply['text'] = 'Voltar'
    # error alert
    def Error():
        self.starting.destroy()
        self.menu.destroy()
        # error widget
        self.result = Frame(self.top)
        self.result.pack()
        error = Label(self.result, fg='Red', height=5, font=('', 15, 'bold'), text='Erro: USB 01')
        error.pack()
    # apply function
    def Apply():
        try:
            self.number = int(self.input.get())
            Result()
            self.uin.pack()
            self.prenum.pack()
            self.nextn.pack()
        except ValueError:
            Error()
            Menu()
            self.apply['command'] = Reset
            self.apply['text'] = 'Voltar'
    # top frame
    self.top = Frame(master)
    self.top.pack()
    # starting window init
    Start()
# application setup
root = Tk()
root.title('<&>')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
