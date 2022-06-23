from cgi import print_arguments
from time import sleep

def cls():
    print("\033[2J\033[;H", end='')
    sleep(0.1)

cls()

print('Hello')
print('Kaka')