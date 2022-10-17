# import system from os
from os import system
# application module
def Application():
    # clear terminal function
    def Clear():
        system('clear')
    # multiplication table
    def Multiply():
        Clear()
        x = 0
        print('Tabuada do número: {}'.format(userInput))
        while x <= 10:
            print('\033[1m{} x {:2d} = \033[33m{:2d}\033[m'.format(userInput, x, userInput * x))
            x += 1
    Clear()
    try:
        # user input
        userInput = int(input('Digite um número para ver sua tabuada.\nNúmero: '))
        Multiply()
    except ValueError:
        Clear()
        print('\033[1:31mErro: USB 01')
# application start
Application()
