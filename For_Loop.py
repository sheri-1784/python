from time import sleep

def cls():
    print("\033[2J\033[;H", end='')
    sleep(0.1)

cls()

#*
#**
#***
#****
#*****

#*****
#*****
#*****
'''
    *
   **
  ***
 ****
*****    
'''

#for(x=0,x<5,x=x+1):
#   print('*',end=' ')
#bac = 0,1,2,3,4

'''
for bac in range(5):
    for val in range(bac+1):
        print('*',end=' ')
    print()
'''


for bac in range(5):
    for val in range(4-bac):
        print('',end='')   
    for duc in range(bac+1):
        print('* ',end='')
    print()

bike = []
for value in range(11):
    bike.append(value)
print(bike)
    
square = []
for val in range(11):
    square.append(val+1)
print(square)

'''
line 0: spaces = 4, stars = 1
line 1: spaces = 3, stars = 2
line 2: spaces = 2, stars = 3
line 3: spaces = 1, stars = 4
line 4: spaces = 0, stars = 5

bac = 0
    val = 0
        *
    val = 1
        **
    val = 2
        ***
    val = 3
        ****
    val = 4
        *****
bac = 1 
    val = 0
        *
    val = 1
        **
    val = 2
        ***
    val = 3
        ****
    val = 4
        *****
bac = 2
'''
print()
for val in range(5):
    for duc in range(val+1):
        print('x',end=' ')
    print()

print()    
bikes = ['3','6']
print(bikes)
bike1 = bikes[0]
bikes[0] = bikes[1]
bikes[1] = bike1
print(bikes)

print()
for val in range(5):
    for duc in range(4-val):
        print(' ',end=' ')
    for luc in range(val+1):
        print(' X',end='')
    print()