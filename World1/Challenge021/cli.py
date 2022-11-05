# importing system from os
from os import system
# application module
def Application():
    system('clear') # clean terminal at program starts
    print('Tocando: \033[1:33mAll I Am\033[m by \033[1:33mDyalla\033[m\n\033[1:33mq\033[m \033[1mpara sair\033[m\n\n\n')
    system('mpg123 ' + 'song.mp3')
# application start
Application()
