from os import system # impoting system from os module
def Application(): # application module
    def Clear(): # clear function # clean terminal
        system('clear') # clean terminal command
    Clear() # clean terminal at program starts
    numbers = [] # numbers list
    print('\033[1:33mInsira três números para ver qual é o menor e qual é o maior.\033[m')
    while len(numbers) < 3:
        try:
            number = int(input('Insira o {}º número: '.format(len(numbers) + 1)))
            Clear()
            numbers.append(number)
        except ValueError:
            Clear()
            print('\033[1:31mErro: USB 01\033[m')
    numbers.sort()
    print('\033[033mMaior número: \033[1m{}\033[m\n\033[33mMenor número: \033[1m{}\033[m'.format(numbers[-1], numbers[0]))
Application() # start application
