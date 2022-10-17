# importing system from os
from os import system
# application module
def Application():
    # function to get user input grade and append to grades list
    def GetGrade():
        grade = float(input('Digite sua nota: '))
        grades.append(grade)
    # clear terminal
    def Clear():
        system('clear')
    Clear()
    # call to action
    print('Ensira suas notas a seguir para calcular a média.')
    running = True
    grades = []
    sum = 0
    Clear()
    while len(grades) < 1:
        try:
            GetGrade()
        except ValueError:
            Clear()
            print('Erro: USB 01')
    while running != False:
        try:
            option = int(input('Selecione uma opção\n(1) = Adicionar outra nota\n(2) = Calcular média\n(3) = Sair\nOpção: '))
            Clear()
            if option != 1 and option != 2 and option != 3:
                print('Erro: USB 02')
            else:
                if option != 3:
                    if option == 1:
                        GetGrade()
                    else:
                        for x in grades:
                            sum += x
                        print('A sua média é = {:.1f}'.format(sum / len(grades)))
                        running = False
                else:
                    Clear()
                    print('Encerrando programa...')
                    running = False
        except ValueError:
            Clear()
            print('Erro: USB 03')
# application start
Application()
