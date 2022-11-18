# importing system from os
from os import system
# importing randint from random
from random import randint
# application module
def Application():
    # clear function
    def Clear():
        system('clear') # clear terminal
    Clear() # clear terminal at program starts
    # computer's choice
    cc = randint(0, 5)
    run = True
    # attempts
    attempts = 0
    while run == True:
        try:
            # user input
            userInput = int(input('"Pensei" em um número entre 0 e 5 tente adivinhar em qual número eu pensei: '))
            Clear()
            if userInput < 0 or userInput > 5:
                print('\033[1:31mNúmero errado.\033[m\nDigite um número entre \033[1m0\033[m e \033[1m5\033[m.\n')
            else:
                if userInput == cc:
                    run = False
                    if attempts == 0:
                        print('\033[1:32mPerfeito!\033[m\n\033[32mVocê acertou na primeira tentativa.\033[m')
                    else:
                        print('\033[32mVocê acertou!\033[m\n\033[33mNúmero de tentativas {}.\033[m'.format(attempts))
                else:
                    print('Número errado.\nTente novamente.\n')
        except ValueError:
            Clear() # clean terminal
            print('\033[1:31mErro: USB 01\033[m\nDigite um número entre \033[1m0\033[m e \033[1m5\033[m\n')
        attempts += 1
# application start
Application()
