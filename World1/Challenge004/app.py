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
        # get user input
        self.text = self.userInput.get('1.0', 'end-1c').strip().split()
        self.startWidget.destroy()
        self.menu.destroy()
        # result widget
        self.result = Frame(self.top)
        self.result.pack()
        # details
        details = Label(self.result, height=3, font=('', 18, 'bold'), text='Detalhes do texto.')
        details.pack()
        # type and length
        tandl = Label(self.result, fg='#cb5017', font=('', 12), text='O texto é do tipo String (str).\nO texto contém {} caracteres.'.format(len(' '.join(self.text))))
        tandl.pack()
        # only numbers
        numbers = Label(self.result, fg='#cb5017', font=('', 12), text='O texto contém apenas números.')
        # only letters
        letters = Label(self.result, fg='#cb5017', font=('', 12), text='O texto contém apenas letras.')
        # alphanumeric
        alphanum = Label(self.result, fg='#cb5017', font=('', 12), text='O texto é alfanumérico')
        # 'captalizing'
        cap = Label(self.result, fg='#cb5017', font=('', 12), text='')
        # if user input is only numbers
        if ''.join(self.text).isnumeric() == True:
            numbers.pack()
        else:
            if ''.join(self.text).isalnum() == True:
                alphanum.pack()
            else:
                letters.pack()
        # if user input neither only uppercase or lowercase
        if ''.join(self.text).isupper() == False and ''.join(self.text).islower() == False:
            cap['text'] = 'O texto contém letras maiúsculas e minúsculas.'
        # if user input is only uppercase
        elif ''.join(self.text).isupper() == True:
            cap['text'] = 'O texto contém apenas letras maiúsculas.'
        # if user input is only lowercase
        else:
            cap['text'] = 'O texto contém apenas letras minúsculas.'
        cap.pack()
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
