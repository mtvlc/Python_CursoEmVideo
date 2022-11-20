# importing system from os
from os import system
# application module
def Application():
    # check function
    def Check(number):
        # checking if number is odd or even
        if number % 2 == 0:
            print('\033[33mO número \033[1m{}\033[m \033[33mé um número \033[1mpar\033[m\033[33m.\033[m'.format(number))
        else:
            print('\033[33mO número \033[1m{}\033[m \033[33mé um número \033[1mímpar\033[m\033[33m.\033[m'.format(number))
    # clear function
    def Clear():
        system('clear') # clean terminal
    Clear() # clean terminal at program starts
    try:
        # user input number
        number = int(input('Insira um número para ver se ele é par ou ímpar: '))
        Clear() # clean terminal
        Check(number) # check number
    except ValueError:
        Clear() # clean terminal
        print('\033[1:31mErro: USB 01\033[m') # print error code
# application start
Application()
