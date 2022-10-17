# import system from os
from os import system
# application module
def Application():
    # clear terminal
    system('clear')
    # call to action
    text = input('Digite alguma coisa em seguida pressione enter: ')
    # string format
    text = text.strip()
    system('clear')
    # input always return a 'str' type object
    print('\n\033[1:33m{}\033[m\n\nÉ do tipo String (str)\n{} caracteres.'.format(text, len(text)))
    # check if text is numeric
    if text.isnumeric() == True:
        print('Somente números.')
    else:
        # check if text is alphabetic
        if text.isalpha() == True:
            print('Somente letras.')
        else:
            # if is neither numeric or alphabetic is alphanumeric
            print('Alfanumérico.')
        # check if text neither upper or lower
        if text.isupper() == False and text.islower() == False:
            print('Contém letras maiúsculas e minúsculas')
        elif text.isupper() == True:
            print('Apenas letras maiúsculas')
        else:
            print('Apenas letras minúsculas')
# application start
Application()
