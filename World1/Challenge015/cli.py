# importing system from os
from os import system
# application module
def Application():
    # calc function
    def Calc(km, days):
        valueKm = km * 0.15
        valueDays = days * 60
        Clear()
        print('Quilômetros percorridos \033[33m{:.1f}\033[m = R$\033[32m{:.2f}\033[m\nDias Alugados \033[33m{}\033[m = R$\033[32m{:.2f}\033[m\n\n\033[1mValor total do aluguel R$\033[1:33m{:.2f}\033[m.'.format(km, valueKm, days, valueDays, valueKm + valueDays))
    # clear function # clean terminal
    def Clear():
        system('clear')
    # clean terminal at program starts
    Clear()
    # call to action
    print('Ensira os dados a seguir para calcular o valor do aluguel.')
    try:
        Clear()
        km = float(input('Quantidade de quilômetros percorridos: '))
        days = int(input('Quantidade de dias alugados: '))
        Calc(km, days)
    except ValueError:
        Clear()
        print('\033[1:31mErro: USB 01\033[m')
# application start
Application()
