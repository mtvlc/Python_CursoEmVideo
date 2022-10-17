# application module
def Application():
    userName = str(input('Ensira seu nome e pressione ENTER: ')).strip().split()
    userName = ' '.join(userName).title()
    welcome = ('\n\033[0;36mBem-Vindo! {}.\033[m'.format(userName))
    print(welcome)
Application()
