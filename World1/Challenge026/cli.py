# importing system from os
from os import system
# application module
def Application():
    # clear function
    def Clear():
        system('clear') # clean terminal
    Clear() # clear terminal at program starts
    phrase = str(input('insira algum texto: '))
    Clear() # clear terminal
    # count A
    print('No texto insirido a letra "\033[1mA\033[m" aparece \033[1:33m{}\033[m vezes.'.format(phrase.upper().count('A')))
    # first
    print('Ela aparece pela primeira vez na posição \033[1:33m{}\033[m.'.format(phrase.upper().find('A') + 1))
    # last
    print('Ela aparece pela última vez na posição \033[1:33m{}\033[m.'.format(phrase.upper().rfind('A') + 1))
# application start
Application()
