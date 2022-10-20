# importing system from os
from os import system
# application module
def Application():
    # clear function # clear terminal
    def Clear():
        system('clear')
    Clear()
    # discount function # give 5% discount to price
    def Discount(price):
        print('O produto que custava R$\033[33m{:.2f}\033[m.\nCom 5% de desconto custará R$\033[32m{:.2f}\033[m.'.format(price, price * 95 / 100))
    # occurs if user input an aceptable value
    try:
        # user input # price
        price = float(input('Ensira o preço do produto que deseja calcular o desconto.\nPreço: R$'))
        Clear()
        Discount(price)
    # occurs if user input a non aceptable value
    except ValueError:
        Clear()
        print('\033[1:31mErro: USB 01')
# application start
Application()
