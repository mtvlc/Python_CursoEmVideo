# import system from os
from os import system
# application module
def Application():
    # clear terminal function
    def Clear():
        system('clear')
    # result module
    def Result():
        print('{} metros equivalem a:\n'.format(meters))
        # units
        km = meters * 0.001
        hm = meters * 0.01
        dam = meters * 0.1
        dm = meters * 10
        cm = meters * 100
        mm = meters * 1000
        # kilometers
        print('{} quilômetros.\n{} hectômetros.\n{} decâmetros.\n{} decímetros.\n{} centímetros.\n{} milímetros.'.format(km, hm, dam, dm, cm, mm))
    Clear()
    # call to action
    print('Digite um valor em metros para mostrar as conversões.')
    try:
        meters = float(input('Metros: '))
        Clear()
        Result()
    except ValueError:
        Clear()
        print('Erro: USB 01')
# application start
Application()
