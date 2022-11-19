# importing system from os
from os import system
# application module
def Application():
    # clear function
    def Clear():
        system('clear') # clean terminal
    Clear() # clean terminal at program starts
    # speed limit
    speedLimit = 80
    try:
        # user input vehicle speed
        vehicleSpeed = int(input('Insira a velocidade que o veículo estava: '))
        Clear() # clean terminal
        if vehicleSpeed > speedLimit:
            print('\033[1:31mVeículo acima do limite permitido!\033[m\n\033[33mValor da multa: R$\033[1m{:.2f}\033[m\033[33m.\033[m'.format((vehicleSpeed - speedLimit) * 7))
        else:
            print('\033[32mVeículo dentro do limite de velocidade.\033[m')
    except ValueError:
        Clear() # clean terminal
        print('\033[1:31mErro: USB 01\033[m')
# application start
Application()
