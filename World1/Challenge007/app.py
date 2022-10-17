# importing system from os
from os import system
# importing graphic library
from tkinter import *
# application module
def Application(self, master=None):
    self.grades = []
    # enter function
    def Enter(event):
        AddGrade()
    # add grade function
    def AddGrade():
        try:
            grade = float(self.grade.get())
            self.grades.append(grade)
            if len(self.grades) <= 1:
                self.status['text'] = 'Nota adicionada!'
                self.status['fg'] = 'green'
            else:
                self.status['text'] = '{} notas adicionadas.'.format(len(self.grades))
                self.status['fg'] = 'green'
        except ValueError:
            print('Erro: USB 01')
            self.status['text'] = 'Erro: USB 01'
            self.status['fg'] = 'red'
    # menu module
    def Menu():
        # menu widget
        self.menu = Frame(self.top)
        self.menu.pack()
        # exit button
        exit = Button(self.menu, command=self.top.quit, text='Sair')
        exit.pack(side=LEFT, padx=(0, 2))
        # add grade button
        self.apply = Button(self.menu, command=AddGrade, text='Adicionar nota')
        self.apply.pack(side=LEFT, padx=(2, 2))
        # calcule average button
        self.calc = Button(self.menu, command=Result, text='Calcular média')
        self.calc.pack(side=LEFT, padx=(2 ,0))
    # starting window module
    def Start():
        # starting window widget
        self.starting = Frame(self.top)
        self.starting.pack()
        # call to action
        cta = Label(self.starting, height=2, font=('', 13), text='Ensira suas notas para calcular a média.')
        cta.pack(pady=(5, 2))
        # status
        self.status = Label(self.starting, text='')
        self.status.pack(pady=(0, 5))
        # user input widget
        self.uiw = Frame(self.starting)
        self.uiw.pack()
        self.grade = Entry(self.uiw, width=4)
        self.grade.insert(END, 7.5)
        self.grade.pack(pady=(0, 15))
        self.grade.bind('<Return>', Enter)
        # start menu
        Menu()
    # result window module
    def Result():
        sum = 0
        for x in self.grades:
            sum += x
        avrg = float(sum / len(self.grades))
        if avrg < 6.0:
            self.status['fg'] = 'red'
        self.status['text'] = 'A sua média é = {:.1f}.'.format(avrg)
    # clear terminal
    system('clear')
    # top frame
    self.top = Frame(master)
    self.top.pack()
    # start window
    Start()
# application setup
root = Tk()
root.title('Average')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
