# importing radians, sin, cos, tan from math
from math import radians, sin, cos, tan
# importing system from os
from os import system
# importing graphic library
from tkinter import *
# application module
def Application(self, master=None):
    # reset function
    def Reset():
        # destroy menu and result widget
        self.result.destroy()
        self.menu.destroy()
        Start() # recreate starting window
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
        exit.pack(side=LEFT, padx=(0, 2))
        # apply button
        self.apply = Button(self.menu, command=Result, text='Calcular')
        self.apply.pack(side=LEFT, padx=(2, 0))
    # starting window module
    def Start():
        # starting window widget
        self.starting = Frame(self.top)
        self.starting.pack()
        # call to action
        cta = Label(self.starting, height=3, font=('', 12), text='Ensira um ângulo abaixo\npara calcular o SENO, COSSENO\ne TANGENTE desse ângulo.')
        cta.pack(pady=(15, 10))
        # user input
        self.angle = Entry(self.starting, width=5)
        self.angle.insert(END, 30)
        self.angle.bind('<Return>', Enter)
        self.angle.pack(pady=(10, 15))
        Menu() # create menu
    # result window module
    def Result():
        # result widget
        self.result = Frame(self.top)
        try:
            angle = float(self.angle.get())
            # result widget
            result = Frame(self.result)
            # angle
            angleLabel = Label(result, font=('', 12), text='Ângulo de {:.1f}º'.format(angle))
            angleLabel.pack(pady=(2, 2))
            # sine
            sine = Label(result, text='Seno = {:.2f}'.format(sin(radians(angle))))
            sine.pack(pady=(2, 2))
            # cosine
            cosine = Label(result, text='Cosseno = {:.2}'.format(cos(radians(angle))))
            cosine.pack(pady=(2, 2))
            # tangent
            tangent = Label(result, text='Tangente = {:.2f}'.format(tan(radians(angle))))
            tangent.pack(pady=(2, 2))
            result.pack(pady=(15, 15))
        except ValueError:
            # error alert
            error = Label(self.result, height=5, fg='red', font=('', 15, 'bold'), text='Erro: USB 01')
            error.pack()
        # destroy menu and starting window
        self.starting.destroy()
        self.menu.destroy()
        self.result.pack()
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
# applicaton setup
root = Tk()
root.title('Sin,Cos,Tan')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
