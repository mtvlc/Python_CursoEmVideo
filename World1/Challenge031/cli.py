# importing system from os
from os import system
# application module
def Application():
    # price calculate function
    def Price(distance):
        if distance <= 0:
            print('\033[1:31mErro: USB 02\033[m')
        else:
            if distance > 200:
                print('Valor da passagem: R$\033[33m{:.2f}\033[m.\nDistância da viagem: \033[33m{}\033[mkm.'.format(distance * 0.45, distance))
            else:
                print('Valor da passgem: R$\033[33m{:.2f}\033[m.\nDistância da viagem: \033[33m{}\033[mkm.'.format(distance * 0.5, distance))
    # clear function
    def Clear():
        system('clear') # clean terminal
    Clear() # clean terminal at program starts
    try:
        # get travel distance
        distance = float(input('Insira a distância da viagem para calcular o valor: '))
        Clear() # clean terminal
        Price(distance) # call price function
    except ValueError:
        Clear() # clean terminal
        print('\033[1:31mErro: USB 01\033[m')
# application start
Application()
