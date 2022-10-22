# importing system from os
from os import system
# application module
def Application():
    # clear function # clean terminal
    def Clear():
        system('clear')
    # clear terminal at program starts
    Clear()
# application start
Application()
