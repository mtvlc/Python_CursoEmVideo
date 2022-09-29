# importing graphic library
from tkinter import *
# application module
def Application(self, master=None):
    # top frame
    top = Frame(master)
    top.pack()
    # menu module
    def Menu():
        # menu widget
        self.menu = Frame(top)
        self.menu.pack()
        # exit button
        exit = Button(self.menu, command=top.quit, text='Sair')
        exit.pack(side=LEFT)
        # back button
        self.back = Button(self.menu, command=Reset, text='Voltar')
    # start window module
    def Start():
        # start window widget
        self.start = Frame(top)
        self.start.pack()
        # call to action
        cta = Label(self.start, height=2, font=('bold', 10), text='Ensira seu nome abaixo em seguida pressione enter.')
        cta.pack(pady=(8,15))
        # user input
        self.name = Entry(self.start, width=20)
        self.name.insert(END, 'Nome')
        self.name.pack(pady=(0,18))
        Menu()
        self.name.bind('<Return>', Result)
    # output window
    def Result(event):
        # get name
        name = self.name.get()
        # string treatement
        name = name.strip().split()
        # wipe start window
        self.start.destroy()
        self.menu.destroy()
        # result window widget
        self.result = Frame(top)
        self.result.pack()
        welcome = Label(self.result, fg='blue', height=3, font=('bold', 12), text='Bem-vindo!\n{}.\n'.format(' '.join(name).title()))
        welcome.pack(pady=(25, 5))
        Menu()
        self.back.pack(side=LEFT)
    # reset function
    def Reset():
        self.start.destroy()
        self.menu.destroy()
        self.result.destroy()
        Start()
    # start program
    Start()
# application setup
root = Tk()
root.title('Welcome!')
root.geometry('400x150')
# application start
Application(root)
# mainloop
root.mainloop()
