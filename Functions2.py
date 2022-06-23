from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()
'''
y = int(input('What No: '))
x = 1
n = 1
while n <= y:
    x = x*n
    n = n+1
print(x)

def fact(n):
    r = 1
    while n > 0:
        r = r*n
        n = n-1
    return(r)
x = fact(int(input('Factor: ')))
print(x)

def power(x,y):
    r = 1
    while y > 0:
        r = r*x
        y = y-1
    return(r)
n = power(x=2,y=14)
print(n)

def learn(name, course):
    print('My name is',name)
    print('I am learning ',course)
learn('kaka','python')

def calc(a,b,c):
    add = (a**b+c)
    return add
num = calc(3,3,3)
print(num)

def numtype(x):

    if x % 2 == 0:
        print('Even Number')
    else:
        print('Odd Number')
numtype(2)
print(numtype.__doc__)

def evenb(elist):
    even = []
    for n in elist:
        if n % 2 == 0:
            even.append(n)
    return(even)
even = evenb([1,2,3,4,5,6,7,8,9])
for eve in even:
    print(eve**2,end=' ')

x = 5
def func1():
    print(x)

def func2():
    global x
    x = 555
    print(x)
    
def func3():
    print(x)
    
func1()
func2()
func3()

def outer():
    x = 777
    def inner():
        nonlocal x
        x = 700
        print('Inner X value is:',x)
    inner()
    print('Outer X value is:',x)
outer()

def add(*number):
    x = 0
    for num in number:
        x = x+num
    return x
a = add(1,2,3,4)
b = add(2,2,2,2)
c = add(4,3,2,1)
print(a)
print(b)
print(c)

def fact(x):
    if x == 0:
        return None
    else:
        return x*fact(x-1)
y = fact(int(input('Number: ')))
print(y)
'''
