# importing os library
import os
# importing datetime library
import datetime
# application module
def Application():
    os.system('clear')
    running = 1
    today = datetime.datetime.now()
    while running != False:
        option = int(input('{}\nEscolha uma opção em seguida pressione enter para continuar.\nEditar (1)\nCalcular idade (2)\nSair (0)\n:'.format(Date())))
        if option > 2 or option < 0:
            print('Erro: USB 04')
            running = False
        elif option == 0:
            running = False
        elif option == 2:
            running = False
            print('Você tem {} anos.'.format(int(today.strftime('%Y')) - Date()[1]))
        else:
            os.system('clear')
# get date function
def Date():
    monthdict = {
    1:'Janeiro',
    2:'Fevereiro',
    3:'Março',
    4:'Abril',
    5:'Maio',
    6:'Junho',
    7:'Julho',
    8:'Agosto',
    9:'Setembro',
    10:'Outubro',
    11:'Novembro',
    12:'Dezembro'
    }
    year = int(input('Digite o ano que você nasceu.\nEx: 1996: '))
    if year > 9999 or year < 0:
        return "Erro: USB 01\n"
    else:
        month = int(input('Digite o mês que você nasceu.\nEx: 10: '))
        if month > 12 or month < 1:
            return 'Erro: USB 02\n'
        else:
            day = int(input('Digite o dia que você nasceu.\nEx: 21: '))
            if day > 31 or day < 1:
                return 'Erro: USB 03\n'
            else:
                return "Você nasceu no dia {} de {} de {}.".format(day, monthdict[month], year)
# application start
Application()
