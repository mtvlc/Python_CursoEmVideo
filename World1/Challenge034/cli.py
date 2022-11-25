from os import system # importing system from os
def Application(): # application module
    def Clear(): # clear function
        system('clear') # clean terminal
    Clear() # clean terminal at program starts
    try:
        salary = float(input('Insira o salário para calcular o aumento: '))
        Clear() # clean terminal
        if salary <= 1250.0: # check if salary is under or equal 1250
            newSalary = salary * 115 / 100 # if true add 15% salary to new salary
        else:
            newSalary = salary * 110 / 100 # if false add 10% salary to new salary
        print('\033[33mValor do salário atual: \033[32mR${:.2f}\n\033[33mValor do salário após ajuste: \033[32mR${:.2f}\n\033[33mValor do aumento: \033[32mR${:.2f}\033[m'.format(salary, newSalary, newSalary - salary)) # print result
    except ValueError: # if value input is not a number print error message
        Clear() # clean terminal
        print('\033[1:31mErro: USB 01\033[m')
Application() # application start
