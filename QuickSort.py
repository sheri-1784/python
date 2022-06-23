from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()

import statistics

def sort(number):
    if len(number) <= 1:
        return number
    else:
        pivot = number[len(number)//2]
        less, equal, great = (
            [n for n in number if n < pivot],
            [n for n in number if n == pivot],
            [n for n in number if n > pivot]
            )
        return (sort(less) 
                + equal 
                + sort(great))

xyz = [2,4,4,3,5,6,8,9,4,3]
m = sort(xyz)
print(m)