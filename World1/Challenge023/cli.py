# importing system from os
from os import system
# application module
def Application():
    # clear function
    def Clear():
        system('clear') # clean terminal
    Clear() # clean terminal at program starts
    golden = ['Unidade          ', 'Unidade Dezena   ', 'Unidade Centena  ', 'Unidade de Milhar']
    number = str(input('Ensira um número entre 0 e 9999: ')).strip()
    Clear()
    try:
        numberInt = int(number)
        if numberInt >= 0 and numberInt <= 9999:
            digits = []
            i = 0
            for x in number:
                digits.append(x)
            digits.reverse()
            for x in digits:
                print('{} \033[1m{}\033[m'.format(golden[i], x))
                i += 1
        else:
            print('\033[1:31mErro: USB 01\033[m\n\033[1:33mEnsira um número entre 0 e 9999.\033[m')
    except ValueError:
        Clear()
        print('\033[1:33mNúmero não reconhecido.\nTente novamente.\033[m')
# application start
Application()
