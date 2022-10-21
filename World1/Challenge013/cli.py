# importing system from os
from os import system
# application module
def Application():
    # clear function # clean terminal
    def Clear():
        system('clear')
    # clean terminal at program starts
    Clear()
    try:
        # user input salary
        salary = float(input('Ensira seu salário para calcular o aumento.\nSalário: R$'))
        # clean terminal
        Clear()
        # print current salary value
        print('O valor do seu salário atual é = R$\033[33m{:.2f}\033[m.'.format(salary))
        # print salary value after increase 15%
        print('O valor do salário após 15% de aumento R$\033[32m{:.2f}\033[m.'.format(salary * 115 / 100))
        # print amount increased
        print('Valor do aumento = R$\033[32m{:.2f}\033[m.'.format(salary * 115 / 100 - salary))
    except ValueError:
        # clean terminal and print error code
        Clear()
        print('\033[1:31mErro: USB 01')
# application start
Application()
