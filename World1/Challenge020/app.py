# importing system from os
from os import system
# importing shuffle from random
from random import shuffle
# importing graphic library
from tkinter import *
# application module
def Application(self, master=None):
    # name handle function
    def NameHandle():
        self.name = self.nameInput.get()
        if self.students.count(self.name) != 0:
            self.students.remove(self.name)
        else:
            self.students.append(self.name)
    # update function
    def Update():
        self.app.destroy()
        self.menu.destroy()
        Start()
    # shuffle function
    def Shuffle():
        shuffle(self.students)
        Update()
    # apply function
    def Apply():
        NameHandle()
        Update()
    # enter event
    def Enter(event):
        NameHandle()
        Update()
    # menu module
    def Menu():
        # menu widget
        self.menu = Frame(self.leftSide)
        # exit button
        exit = Button(self.menu, command=self.top.quit, text='Sair')
        exit.pack(side=LEFT, padx=(0, 2))
        # apply button
        self.apply = Button(self.menu, command=Apply, text='Cadastrar')
        self.apply.pack(side=LEFT, padx=(2, 0))
        self.menu.pack()
        # shuffle button
        self.shuffle = Button(self.menu, command=Shuffle, text='Sortear')
        self.shuffle.pack()
    # starting window module
    def Start():
        # application widget
        self.app = Frame(self.top)
        # left side
        self.leftSide = Frame(self.app)
        # call to action
        self.cta = Label(self.leftSide, height=2, font=('', 12, 'bold'), text='Cadastrar Aluno')
        self.cta.pack()
        # user input
        self.nameInput = Entry(self.leftSide, width=10)
        self.nameInput.insert(END, 'Aluno(a)')
        self.nameInput.bind('<Return>', Enter)
        self.nameInput.pack(pady=(0, 12))
        self.leftSide.pack(side=LEFT, padx=(0, 20), pady=(30, 0)) # render leftside widget
        Menu() # create menu
        self.rightSide = Frame(self.app) # create rightside widget
        namesLabel = Label(self.rightSide, height=3, font=('', 10, 'bold'), text='Ordem de\napresentação')
        namesLabel.pack() # render nameslabel
        for i in range(len(self.students)): # create student name list
            name = Label(self.rightSide, text='{}º - {}'.format(i + 1, self.students[i]))
            name.pack() # render name
        self.rightSide.pack(side=LEFT, padx=(20, 0)) # render rightside widget
        self.app.pack() # render app widget
    system('clear') # clean terminal at program starts
    self.students = [] # students list
    self.top = Frame(master) # create application top frame
    Start() # create starting window
    self.top.pack() # render top frame
# application setup
root = Tk()
root.title('Shuffle')
root.geometry('400x250')
# application start
Application(root)
# mainloop
root.mainloop()
