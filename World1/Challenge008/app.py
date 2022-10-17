# importing graphic library
from tkinter import *
# importing system from os
from os import system
# application module
def Application(self, master=None):
    # reset function
    def Reset():
        self.starting.destroy()
        self.menu.destroy()
        self.result.destroy()
        Start()
    # enter function event
    def Enter(event):
        Result()
    # calc function
    def Calc():
        try:
            # user input meters
            self.meters = float(self.userInput.get())
            # km
            self.km = self.meters * 0.001
            # hm
            self.hm = self.meters * 0.01
            # dam
            self.dam = self.meters * 0.1
            # dm
            self.dm = self.meters * 10
            # cm
            self.cm = self.meters * 100
            # mm
            self.mm = self.meters * 1000
        except ValueError:
            self.meters = None
    # menu module
    def Menu():
        # menu widget
        self.menu = Frame(self.top)
        self.menu.pack()
        # exit button
        exit = Button(self.menu, command=self.top.quit, text='Sair')
        exit.pack(side=LEFT, padx=(0, 2))
        # apply button
        self.apply = Button(self.menu, command=Result, text='Converter')
        self.apply.pack(side=LEFT, padx=(2, 0))
    # starting window module
    def Start():
        # starting window module
        self.starting = Frame(self.top)
        self.starting.pack()
        # call to action
        cta = Label(self.starting, height=3, font=('', 13, 'bold'), text='Digite um valor em metros abaixo\npara converter.')
        cta.pack()
        # user input
        self.userInput = Entry(self.starting, width=15)
        self.userInput.insert(END, 78.5)
        self.userInput.pack(pady=(10, 25))
        self.userInput.bind('<Return>', Enter)
        # menu
        Menu()
    # result window module
    def Result():
        Calc()
        # destroy starting window
        self.starting.destroy()
        self.menu.destroy()
        # result window widget
        self.result = Frame(self.top)
        self.result.pack()
        # upper frame
        self.upper = Frame(self.result)
        # lower frame
        self.lower = Frame(self.result)
        if self.meters != None and self.meters != 0:
            meters = Label(self.result, text='{} metros equivalem a:'.format(self.meters))
            meters.pack(side=TOP, pady=(10, 5))
            # km
            km = Label(self.upper, text='')
            if self.km == 1:
                km['text'] = '{:.0f} quilômetro'.format(self.km)
            else:
                km['text'] = '{:.2f} quilômetros'.format(self.km)
            km.pack()
            # hm
            hm = Label(self.upper, text='')
            if self.hm == 1:
                hm['text'] = '{:.0f} hectômetro'.format(self.hm)
            else:
                hm['text'] = '{:.2f} hectômetros'.format(self.hm)
            hm.pack()
            # dam
            dam = Label(self.upper, text='')
            if self.dam == 1:
                dam['text'] = '{:.0f} decâmetro'.format(self.dam)
            else:
                dam['text'] = '{:.2f} decâmetros'.format(self.dam)
            dam.pack()
            # m
            m = Label(self.result, text='')
            if self.meters == 1:
                m['text'] = '{:.0f} metro'.format(self.meters)
                m['fg'] = 'green'
            else:
                m['text'] = '{:.2f} metros'.format(self.meters)
                m['fg'] = 'green'
            m.pack(side=BOTTOM, pady=(0, 5))
            # dm
            dm = Label(self.lower, text='')
            if self.dm == 1:
                dm['text'] = '{:.0f} decímetro'.format(self.dm)
            else:
                dm['text'] = '{:.2f} decímetros'.format(self.dm)
            dm.pack()
            # cm
            cm = Label(self.lower, text='')
            if self.cm == 1:
                cm['text'] = '{:.0f} centímetro'.format(self.cm)
            else:
                cm['text'] = '{:.2f} centímetros'.format(self.cm)
            cm.pack()
            # mm
            mm = Label(self.lower, text='')
            if self.mm == 1:
                mm['text'] = '{:.0f} milímetro'.format(self.mmm)
            else:
                mm['text'] = '{:.2f} milímetros'.format(self.mm)
            mm.pack()
            self.upper.pack(side=LEFT, pady=(5, 5), padx=(5, 5))
            self.lower.pack(side=LEFT, pady=(5, 5), padx=(5, 5))
        else:
            error = Label(self.result, fg='red', height=4, font=('', 15, 'bold'), text='Erro: USB 01')
            error.pack(pady=(10, 15))
        Menu()
        self.apply['command'] = Reset
        self.apply['text'] = 'Voltar'
    # clear terminal
    system('clear')
    # top frame
    self.top = Frame(master)
    self.top.pack()
    # start window
    Start()
# application setup
root = Tk()
root.title('lengthunit')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
