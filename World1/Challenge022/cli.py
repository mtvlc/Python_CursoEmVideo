# importing system from os
from os import system
# application module
def Application():
    # clear function
    def Clear():
        system('clear') # clean terminal
    Clear() # clean terminal at program starts
# application start
Application()
