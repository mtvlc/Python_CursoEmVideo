# importing system from os
from os import system
# application module
def Application():
    # clear function # clear terminal
    def Clear():
        system('clear')
    # clean terminal at program starts
    Clear()
    # description
    print('Ensira o cateto oposto e o cateto adjacente de um triângulo retângulo para calcular a hipotenusa.')
    try:
        catetoOposto = float(input('Cateto Oposto: '))
        catetoAdjacente = float(input('Cateto Adjacente: '))
        hipotenusa = pow(pow(catetoOposto, 2.0) + pow(catetoAdjacente, 2.0), 0.5)
        Clear() # clean terminal
        print('O comprimento da hipotenusa é = \033[1:33m{:.2f}\033[m.'.format(hipotenusa))
    except ValueError:
        Clear()
        print('\033[1:31mErro: USB 01\033[m')
# application start
Application()
