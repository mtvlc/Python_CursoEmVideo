# importing system from os
from os import system
# application module
def Application():
    # clear function
    def Clear():
        system('clear') # clean terminal
    Clear() # clean terminal at program starts
    # get name
    name = str(input('Ensira seu nome: ')).strip().upper().split()
    Clear() # clean terminal
    # upper
    print('\033[33mNome com letras maiúsculas\033[m\n\033[1m{}\033[m'.format(' '.join(name)))
    # lower
    print('\033[33mNome com letras minúsculas\033[m\n\033[1m{}\033[m'.format(' '.join(name).lower()))
    # characters
    print('\033[33mTotal de caracteres:\033[m\n\033[1m{}\033[m'.format(len(''.join(name))))
    # characters first name
    print('\033[33mO primeiro nome contém\033[m \033[1m{}\033[m \033[33mletras.\033[m'.format(len(name[0])))
# application start
Application()
