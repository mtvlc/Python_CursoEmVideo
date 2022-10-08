# import system from os
from os import system
# application module
def Application():
    # clear terminal
    system('clear')
    # color
    style = {
        'Yellow': '\033[33m',
        'Red': '\033[31m',
        'Bold': '\033[1m',
        'Green': '\033[4;32m',
        'Clear': '\033[m'
    }
    try:
        # get user input number
        number = int(input('{}{}{}'.format(style['Bold'], 'Digite um número: ', style['Clear'])))
        # clear terminal
        system('clear')
        # print the predecessor and the successor of the user input number
        print('{}{}{}{}{}{}.\n\n{}{}{}{}{}{}{}{}{}{}{}.\n{}{}{}{}{}{}{}{}{}.'.format(style['Bold'], 'Você enseriu o número ', style['Yellow'], number, style['Clear'], style['Bold'], style['Clear'], style['Green'], style['Bold'], number - 1, style['Clear'], style['Yellow'],  ' é o antecessor de ', style['Bold'], number, style['Clear'], style['Bold'], style['Green'], number + 1, style['Clear'], style['Yellow'], ' é o sucessor de ', style['Bold'], number, style['Clear'], style['Bold']))
    except ValueError:
        # print erro if user input is not an int number
        print('{}{}'.format(style['Red'], 'Erro: USB 01'))
# application start
Application()
