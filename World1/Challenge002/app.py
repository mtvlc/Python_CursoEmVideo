# importing datetime library
import datetime
# importing os > system module
from os import system
# importing graphic library
from tkinter import *
from tkinter import ttk
# application module
def Application(self, master=None):
    system('clear')
    # menu
    def Menu():
        # menu widget
        self.menu = Frame(self.top)
        self.menu.pack()
        # exit button
        exit = Button(self.menu, command=self.top.quit, text='Sair')
        exit.pack(
            side=LEFT,
            padx=(0, 4)
        )
        # apply button
        self.apply = Button(self.menu, command=Result, text='Continuar')
        self.apply.pack(
            side=LEFT,
            padx=(4, 0)
        )
    # reset
    def Reset():
        self.start.destroy()
        self.menu.destroy()
        self.result.destroy()
        Start()
    # Countdown
    def Countdown():
        dob = datetime.datetime(int(self.today.strftime('%Y')), int(self.date[1]), int(self.date[2]))
        calc = str(dob - self.today).split()
        if calc[0][0] != '-':
            count = Label(self.result, height=2, fg='green', font=('Times New Roman', 15), text='Faltam {} dias para seu {}º aniversário'.format(calc[0], int(self.today.strftime('%Y')) - self.year))
        else:
            calc = str(self.today - dob).split()
            count = Label(self.result, height=2, fg='green', font=('Times New Roman', 15), text='Faltam {} dias para seu {}º aniversário.'.format(calc[0], int(self.today.strftime('%Y')) + 1 - self.year))
        count.pack(pady=(0, 8))
    # Start window
    def Start():
        days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
        months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        # start window widget
        self.start = Frame(self.top)
        self.start.pack()
        # call to action
        cta = Label(self.start, height=4, font=('bold', 12), text='Ensira sua data de nascimento abaixo\nem seguida clique em continuar.')
        cta.pack()
        # user input widget
        self.userInput = Frame(self.start)
        self.userInput.pack()
        # day
        self.day = ttk.Combobox(self.userInput, width=4, values=days)
        self.day.set('Dia')
        self.day.pack(
            side=LEFT,
            pady=(0, 20),
            padx=(0, 8)
        )
        # month
        self.month = ttk.Combobox(self.userInput, width=10, values=months)
        self.month.set('Mês')
        self.month.pack(
            side=LEFT,
            pady=(0, 20),
            padx=(4, 4)
        )
        # year
        self.year = Entry(self.userInput, width=5)
        self.year.insert(END, 'Ano')
        self.year.pack(
            side=LEFT,
            pady=(0, 20),
            padx=(8, 0)
        )
        Menu()
    # result window
    def Result():
        self.today = datetime.datetime.now()
        monthdict = {
            'Janeiro': 1,
            'Fevereiro': 2,
            'Março': 3,
            'Abril': 4,
            'Maio': 5,
            'Junho': 6,
            'Julho': 7,
            'Agosto': 8,
            'Setembro': 9,
            'Outubro': 10,
            'Novembro': 11,
            'Dezembro': 12
        }
        self.date = []
        self.year = int(self.year.get())
        self.date.append(self.year)
        month = str(self.month.get())
        self.date.append(month)
        self.date[-1] = monthdict[month]
        day = int(self.day.get())
        self.date.append(day)
        self.start.destroy()
        self.menu.destroy()
        # result window widget
        self.result = Frame(self.top)
        self.result.pack()
        # result label
        result = Label(self.result, height=4, fg='green', font=('bold', 12), text='Você nasceu no dia {}\nde {} do ano {}.\n{} anos.'.format(self.date[-1], month, self.date[0], int(self.today.strftime('%Y')) - self.year))
        result.pack()
        Countdown()
        Menu()
        self.apply['command'] = Reset
        self.apply['text'] = 'Voltar'
    # top frame
    self.top = Frame(master)
    self.top.pack()
    # init start window
    Start()
# application setup
root = Tk()
root.title('Aniversário!')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
