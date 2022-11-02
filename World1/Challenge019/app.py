# importing system from os
from os import system
# importing choice from random
from random import choice
# importing graphic library
from tkinter import *
# importing messagebox from tkinter
import tkinter.messagebox
# application module
def Application(self, master=None):
    # students list
    self.students = []
    # choice function
    def Choice():
        try:
            tkinter.messagebox.showinfo('Winner', 'O Aluno(a) escolhido foi {}'.format(choice(self.students)))
        except IndexError:
            tkinter.messagebox.showerror('USB 03', 'A lista de sorteio está vazia')
    # list function
    def List():
        if len(self.students) == 0:
            tkinter.messagebox.showinfo('Students', 'Nenhum aluno cadastrado')
        else:
            tkinter.messagebox.showinfo('Students', self.students)
    # enter event
    def Enter(event):
        name = self.name.get()
        if name == '':
            self.students.clear()
        else:
            if self.students.count(name) != 0:
                self.students.remove(name)
            else:
                self.students.append(name)
    # delete function
    def Del():
        name = self.name.get()
        try:
            self.students.remove(name)
        except ValueError:
            tkinter.messagebox.showerror('USB 01', 'Não foi possível remover, aluno não cadastrado.')
    # add function
    def Add():
        name = self.name.get()
        if self.students.count(name) != 0:
            tkinter.messagebox.showerror('USB 02', 'Aluno já cadastrado.')
        else:
            self.students.append(name)
    # menu module
    def Menu():
        self.menu = Frame(self.top)
        self.menu.pack(pady=(5, 0))
        # exit button
        exit = Button(self.menu, command=self.top.quit, text='Sair')
        exit.pack(side=LEFT, padx=(0, 2))
        # choice button
        choice = Button(self.menu, command=Choice, text='Sortear')
        choice.pack(side=LEFT, padx=(2, 0))
    # starting window module
    def Start():
        # starting window widget
        self.starting = Frame(self.top)
        # call to action
        cta = Label(self.starting, height=3, font=('', 12, 'bold'), text='Ensira os nomes dos alunos em\nseguida clique me Sortear')
        cta.pack()
        # name entry
        self.name = Entry(self.starting, width=12)
        self.name.insert(END, 'Aluno(a)')
        self.name.bind('<Return>', Enter)
        self.name.pack(pady=(10, 0))
        # crud menu
        menu = Frame(self.starting)
        # list button
        list = Button(menu, command=List, text='Lista')
        list.pack(side=LEFT, padx=(0 ,2))
        # add button
        add = Button(menu, command=Add, text='Adicionar')
        add.pack(side=LEFT, padx=(2, 2))
        # delete button
        delete = Button(menu, command=Del, text='Remover')
        delete.pack(side=LEFT, padx=(2, 0))
        menu.pack(pady=(15, 0))
        self.starting.pack(pady=(5, 5))
        Menu() # create menu
    system('clear') # clean terminal at program starts
    self.top = Frame(master) # top frame
    self.top.pack()
    Start() # crate starting window
# application setup
root = Tk()
root.title('Random')
root.geometry('400x200')
# applicaton start
Application(root)
# mainloop
root.mainloop()
