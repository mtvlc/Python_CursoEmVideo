# importing shuffle from random
from random import shuffle
# importing system from os
from os import system
# application module
def Application():
    # getnames function
    def GetNames(): # get four students names and send to students list
        while len(students) < 4:
            name = str(input('Ensira o nome do {}º aluno(a) para cadastrar: '.format(len(students) + 1))) # get student name
            students.append(name)
            Clear() # clean terminal
    def Clear(): # clean terminal function
        system('clear')
    Clear() # clear terminal at program starts
    students = [] # students list
    GetNames()
    print('\n\033[1:33mAlunos registrados\033[m')
    for x in students:
        print(x)
    shuffle(students)
    print('\n\033[1:33mOrdem de apresentação\033[m')
    for i in students:
        print(i)
# start application:
Application()
