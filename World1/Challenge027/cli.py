# importing system from os
from os import system
# application module
def Application():
    # clear function
    def Clear():
        system('clear') # clean terminal
    Clear() # clean terminal at program starts
    # get name
    name = str(input('Nome Completo: ')).strip().title().split()
    Clear() # clear terminal
    # result
    if len(name) != 1:
        print('\033[1mPrimeiro nome: \033[33m{}\033[m\n\033[1m  Último nome: \033[33m{}\033[m'.format(name[0], name[-1]))
    else:
        print('\033[1mPrimeiro nome: \033[33m{}\033[m'.format(name[0]))
# application start
Application()
