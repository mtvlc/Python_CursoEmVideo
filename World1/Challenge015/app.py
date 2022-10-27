# importing system from os
from os import system
# importing graphic library
from tkinter import *
# importing messagebox from tkinter
import tkinter.messagebox
# application module
def Application(self, master=None):
    # reset function
    def Reset():
        # destroy windows
        self.result.destroy()
        self.menu.destroy()
        Start()
    # error message
    def Error():
        tkinter.messagebox.showerror('Error!', 'Erro: USB 01')
    # price message
    def Price():
        tkinter.messagebox.showinfo('Price Table', 'R$00.15 por quilômetro\nR$60.00 diária')
    # menu module
    def Menu():
        # menu widget
        self.menu = Frame(self.top)
        self.menu.pack(pady=(20, 5))
        # exit button
        exit = Button(self.menu, command=self.top.quit, text='Sair')
        exit.pack(side=LEFT)
        # price button
        price = Button(self.menu, command=Price, text='Preço')
        price.pack(side=LEFT)
        # apply button
        self.apply = Button(self.menu, command=Result, text='Calcular')
        self.apply.pack(side=LEFT)
    # starting window module
    def Start():
        # staring window widget
        self.starting = Frame(self.top)
        self.starting.pack()
        # call to action
        cta = Label(self.starting, height=3, font=('', 13), text='Ensira os valores abaixo\npara calcular o aluguel.')
        cta.pack(pady=(0, 15))
        # km widget
        km = Frame(self.starting)
        km.pack()
        # km label
        kmLabel = Label(km, text='Quilômetros rodados')
        kmLabel.pack(side=LEFT)
        # km entry
        self.km = Entry(km, width=10)
        self.km.insert(END, 120)
        self.km.pack(side=LEFT)
        # days widget
        days = Frame(self.starting)
        days.pack()
        # days label
        daysLabel = Label(days, text='Dias alugados')
        daysLabel.pack(side=LEFT, padx=(0, 45))
        # days entry
        self.days = Entry(days, width=10)
        self.days.insert(END, 10)
        self.days.pack(side=LEFT, pady=(0, 10))
        # create menu
        Menu()
    # result window
    def Result():
        # result widget
        self.result = Frame(self.top)
        self.result.pack()
        try:
            # get user input days and km
            day = int(self.days.get())
            km = float(self.km.get())
            # destroy starting window and menu
            self.starting.destroy()
            self.menu.destroy()
            # km widget
            kmw = Frame(self.result)
            kmw.pack()
            # km label
            kmLabel = Label(kmw, fg='purple', font=('', 12), text='Quilômetros rodados:')
            kmLabel.pack()
            # km count
            kmCount = Label(kmw, fg='#505050', font=('', 12, 'bold'), text='{:.1f} = R$'.format(km))
            kmCount.pack(side=LEFT, padx=(5, 5))
            # km value
            kmValue = Label(kmw, fg='green', font=('', 12, 'bold'), text='{:.2f}'.format(km * 0.15))
            kmValue.pack(side=LEFT)
            # days widget
            dw = Frame(self.result)
            dw.pack()
            # days label
            dayLabel = Label(dw, fg='purple', font=('', 12), text='Dias alugados:')
            dayLabel.pack()
            # days count
            daysCount = Label(dw, fg='#505050', font=('', 12, 'bold'), text='{} = R$'.format(day))
            daysCount.pack(side=LEFT)
            # days value
            daysValue = Label(dw, fg='green', font=('', 12, 'bold'), text='{:.2f}'.format(day * 60))
            daysValue.pack(side=LEFT)
            # total
            totalLabel = Label(self.result, fg='purple', font=('', 12), text='Total a pagar:')
            totalLabel.pack()
            # currency
            currency = Label(self.result, fg='#505050', font=('', 12, 'bold'), text='R$')
            currency.pack(side=LEFT, padx=(40, 5))
            # total value
            totalValue = Label(self.result, fg='green', font=('', 12, 'bold'), text='{:.2f}'.format((day * 60) + (km * 0.15)))
            totalValue.pack(side=LEFT)
            Menu()
            # set apply button to reset function
            self.apply['command'] = Reset
            self.apply['text'] = 'Voltar'
        except ValueError:
            Error()
            # blow up menu and windows
            self.starting.destroy()
            self.menu.destroy()
            self.result.destroy()
            Start()
    # clear terminal at program starts
    system('clear')
    # top frame
    self.top = Frame(master)
    self.top.pack()
    # create starting window
    Start()
# application setup
root = Tk()
root.title('CarRent')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
