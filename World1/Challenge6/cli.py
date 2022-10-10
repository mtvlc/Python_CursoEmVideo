# importing system from os
from os import system
# application module
def Application():
    # style
    style = {
        'red': '\033[1:31m',
        'yellow': '\033[33m',
        'clear': '\033[m'
    }
    # clear terminal
    system('clear')
    # call to action
    print('Ensira um número abaixo para ver seu dobro, triplo e raiz quadrada.')
    try:
        # user input number
        number = float(input('Número: '))
        # clear terminal
        system('clear')
        # if user input an int number
        if float.is_integer(number):
            number = int(number)
        # double
        print('{}{}{}{}{}{}{}{}.\n'.format('O dobro de ', style['yellow'], number, style['clear'], ' é = ', style['yellow'], number * 2, style['clear']))
        # triple
        print('{}{}{}{}{}{}{}{}.\n'.format('O triplo de ', style['yellow'], number, style['clear'], ' é = ', style['yellow'], number * 3, style['clear']))
        # square root
        print('{}{}{}{}{}{}{:.2f}{}.\n'.format('A raiz quadrada de ', style['yellow'], number, style['clear'], ' é = ', style['yellow'], number ** 0.5, style['clear']))
    except ValueError:
        print('{}{}'.format(style['red'], 'Erro: USB 01.'))
# application start
Application()
