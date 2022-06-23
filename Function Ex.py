from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()
'''
def bio(name,age):
    print('His name is',name.title())
    print('And his age is',age)
    
bio('kaka',27)

def func(*num):
    x = 0
    for a in num:
        x = x+a
    return x
y = func(1,2,3,4,5,6,7,8)
print(y)

def abc(x,y):
    add = x+y
    mint = x-y
    return add, mint

res = abc(40,10)
for c in res:
    print(c,end=' ')

def emp(name,salary = 9000):
    print('Name:',name.title())
    print('Salary:',salary)

emp('ben')
emp('Ken',12000)
emp('men',salary = 10000)

def even(num):
    dum = []
    for x in num:
        if x % 2 == 0:
            dum.append(x)
    return dum
y = even(list(range(10)))
print(y)
'''

num = [1,2,3,4,5]
print(num)
def zarb_10(x):
    for x in range(len(num)):
        num[x] *= 10
    
zarb_10(num)
print(num)
        