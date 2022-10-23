# importing system from os
from os import system
# application module
def Application():
    # clear function # clean terminal
    def Clear():
        system('clear')
    # clear terminal at program starts
    Clear()
    # try to get a valid input and print result
    try:
        # get degrees celsius
        celsius = float(input('Ensira uma temperatura para convertê-la para ºF.\nCelcius: º'))
        # clear terminal
        Clear()
        if celsius == 1:
            print('\033[1:33m{:.1f}\033[mºC equivale a \033[1:33m{:.1f}\033[mºF.'.format(celsius, celsius * 1.800 + 32.00))
        else:
            print('\033[1:33m{:.1f}\033[mºC equivalem a \033[1:33m{:.1f}\033[mºF.'.format(celsius, celsius * 1.800 + 32.00))
    # clean terminal and print error message
    except ValueError:
        Clear()
        print('\033[1:31mErro: USB 01\033[m')
# application start
Application()
