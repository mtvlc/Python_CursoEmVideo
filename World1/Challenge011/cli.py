# importing system from os
from os import system
# application module
def Application():
    # clear function
    def Clear():
        system('clear')
    Clear()
    # call to action
    print('Ensira as dimensões (largura, altura) da parede para calcular a quantidade de tinta necessária para pintá-la.')
    try:
        # user input
        width = float(input('Largura: '))
        height = float(input('Altura: '))
        area = width * height
        Clear()
        # result
        print('Para uma área de \033[33m{}\033[mm² serão necessários \033[33m{}\033[ml de tinta.'.format(area, area / 2))
    except ValueError:
        Clear()
        print('\033[1:31mErro: USB 01')
# application start
Application()
