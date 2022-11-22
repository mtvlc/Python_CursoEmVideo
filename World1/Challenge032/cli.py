# importing system from os
from os import system
# importing datetime from datetime
from datetime import datetime
# application module
def Application():
    # clear function
    def Clear():
        system('clear') # clean terminal
    Clear() # clean terminal at program starts
    currentYear = datetime.now().year # get currente year
    try:
        # user input year
        year = int(input('Insira um ano para ver se o mesmo é ou não bissexto: '))
        Clear()
        if year % 4 == 0:
            if year % 100 != 0:
                leap = True
            else:
                leap = False
        elif year % 400 == 0:
            leap = True
        else:
            leap = False
        if year == currentYear:
            if leap == True:
                print('{} \033[32mé um ano bissexto.\033[m'.format(year))
            else:
                print('{} \033[33mnão é um ano bissexto.\033[m'.format(year))
        elif year > currentYear:
            if leap == True:
                print('{} \033[32mserá um ano bissexto.\033[m'.format(year))
            else:
                print('{} \033[33mnão será um ano bissexto.\033[m'.format(year))
        else:
            if leap == True:
                print('{} \033[32mfoi um ano bissexto.\033[m'.format(year))
            else:
                print('{} \033[33mnão foi um ano bissexto.\033[m'.format(year))
    except ValueError:
        Clear()
        print('\033[1:31mErro: USB 01\033[m\nAno não reconhecido tente novamente.')
# applicaton start
Application()
