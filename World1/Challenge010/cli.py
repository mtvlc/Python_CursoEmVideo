# importing requests
import requests
# importing json
import json
# importing system from os
from os import system
# application module
def Application():
    # clear function
    def Clear():
        system('clear')
    # get dolar price
    def Dolar(brl):
        # access api
        api = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
        # api return
        value = api.json()
        # price
        price = value['USD']['bid']
        Clear()
        print('Com \033[32mR${:.2f}\033[m você pode comprar \033[32mUS${:.2f}\033[m.'.format(brl, brl / float(price)))
    Clear()
    try:
        brl = float(input('Ensira um valor em reais para converter para dólares americanos.\nR$:'))
        Dolar(brl)
    except ValueError:
        print('\033[1:31mErro: USB 01')
# application start
Application()
