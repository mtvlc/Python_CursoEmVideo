# importing radians, sin, cos, tan from math
from math import radians, sin, cos, tan
# importing system from os
from os import system
# application module
def Application():
    # clear function # clean terminal
    def Clear():
        system('clear')
    # clean terminal at program starts
    Clear()
    try: # get angle and print sen, cos, and tan
        angle = float(input('Ensira um ângulo para mostrar seu \033[33mseno\033[m, \033[33mcosseno\033[m e \033[33mtangente\033[m:'))
        Clear()
        print('Ângulo de {:.1f}º'.format(angle))
        print('Seno     = {:.2f}\nCosseno  = {:.2f}\nTangente = {:.2f}'.format(sin(radians(angle)), cos(radians(angle)), tan(radians(angle))))
    except ValueError: # clean terminal and print error code
        Clear()
        print('\033[1:31mErro: USB 01\033[m')
# application start
Application()
