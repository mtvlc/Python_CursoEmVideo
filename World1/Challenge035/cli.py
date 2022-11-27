from os import system # importing system from os
def Application(): # application module
    def Clear(): # clear function # clean terminal
        system('clear')
    Clear() # clean terminal at program starts
    lines = [] # lines length list
    print('insira o comprimento de 3 retas para calcular se é possível formar um triângulo.') # description
    while len(lines) < 3:
        try:
            line = float(input('Insira o comprimento da {}ª reta: '.format(len(lines) + 1))) # user input line length
            Clear()
            lines.append(line) # add line to lines length list
        except ValueError: # clean terminal and print error message
            Clear()
            print('\033[1:31mErro: USB 01\033[m\n\033[33mComprimento inválido.\033[m')
    lines.sort() # sort lines length list
    if lines[0] + lines[1] > lines[-1]: # print if is a triangle is possible or not
        print('\033[32mÉ possível formar um triângulo.\033[m')
    else:
        print('\033[33mNão é possível formar um triângulo.\033[m')
Application() # application start
