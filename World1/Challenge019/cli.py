# importing system from os
from os import system
# importing choice from random
from random import choice
# application module
def Application():
    # clear fuction
    def Clear(): # clean terminal
        system('clear')
    Clear() # clean terminal at program starts
    students = [] # students list
    while len(students) < 4:
        name = str(input('Ensira o nome do {}º aluno(a): '.format(len(students) + 1))) # get student name
        students.append(name) # insert student name in students list
        Clear() # clean terminal
    print('Alunos selecionados:')
    for x in students: # print students list names
        print(x)
    print('\nO aluno sorteado foi \033[1:33m{}\033[m!'.format(choice(students)))
# application start
Application()
