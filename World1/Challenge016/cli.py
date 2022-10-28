# importing truncate from math
from math import trunc
# importing system from from os
from os import system
# application module
def Application():
    # clean function # clear terminal
    def Clear():
        system('clear')
    # clean terminal at program starts
    Clear()
    try: # get user input float number and print result
        number = float(input('Ensira um número: '))
        Clear() # clean terminal
        print('A parte inteira do número \033[33m{}\033[m é \033[1:33m{}\033[m!'.format(number, trunc(number)))
    except ValueError: # clear terminal and print error code
        Clear()
        print('\033[1:31mErro: USB 01\033[m')
# application start
Application()
