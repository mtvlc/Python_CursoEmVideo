# importing system from os
from os import system
# application module
def Application():
    # clear function # clean terminal
    def Clear():
        system('clear')
    Clear() # clean terminal at program starts
    city = str(input('Ensira o nome de uma cidade: ')).strip().split()
    if city[0].upper() == 'SANTO':
        Clear()
        print('\033[32mO nome da cidade\033[m \033[1m{}\033[m \033[32mcomeça com\033[m \033[1mSanto.\033[m'.format(' '.join(city)))
    else:
        Clear()
        print('\033[33mO nome da cidade\033[m \033[1m{}\033[m \033[33mnão começa com\033[m \033[1mSanto.\033[m'.format(' '.join(city)))
# application start
Application()
