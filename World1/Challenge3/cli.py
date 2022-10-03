from os import system
# application module
def Application():
    system('clear')
    def Calc(x, y):
        if float.is_integer(x) and float.is_integer(y) == True:
            print('\n\033[1mO resultado da soma entre \033[1:33m{}\033[m \033[1mmais\033[m \033[1:33m{}\033[m \033[1mé =\033[1m \033[1:34m{}\033[m.'.format(int(x), int(y), int(x + y)))
        else:
            print('\n\033[1mO resultado da soma entre \033[1:33m{:.2f}\033[m \033[1mmais\033[m \033[1:33m{:.2f}\033[m \033[1mé =\033[1m \033[1:34m{:.2f}\033[m.'.format(x, y, x + y))
    print('Ensira dois números abaixo, para calcular a soma entre eles.\n')
    # first number
    try:
        x = float(input('Primeiro número: '))
        y = float(input('Segundo Número: '))
        Calc(x, y)
    except ValueError:
        print('\033[1:31mErro: USB 01.\nPrograma finalizado')
# application start
Application()
