# importing system from os
from os import system
# application module
def Application():
    # clear function
    def Clear():
        system('clear') # clean terminal
    Clear() # clean terminal at program starts
    # get name
    name = str(input('Ensira o nome para verificar se o mesmo contém "Silva": ')).strip().upper()
    Clear() # clean terminal
    if name.find('SILVA') >= 0:
        print('\033[32mO nome contém \033[1m"Silva"\033[m\033[32m!\033[m')
    else:
        print('\033[33mO nome não contém \033[1m"Silva"\033[m\033[33m.\033[m')
# applicaton start
Application()
