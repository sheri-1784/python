from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()

'''
x = 1
#y = x == 1
if x == 1:
    print(1)
else:
    print(2)

x = 1
while x <= 5:
    print(x)
    x = x+1
print('successfully printed all 5 numbers')

message = ''
while message != 'quit':
    message = input('What do you say now: ')
    print(message)
   
prompt = '\nTell me something, and I will repeat it back to you:'
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
     
message = input('k ')
while True:
    if message == 'hello':
        message = input('What do you say now: ')
        print(message)
        break
print('World')

x = 0
while x < 10:
    x += 1
    if x % 2 != 0:
        continue #skips the condition above
    print(x)

user = ['kaka', 'mama', 'jama']
user.append('makha')
user.insert(0,'dada')
cuser = []

while user:
    cuser.append(user.pop())
print('Verified users are:')

cuser.sort()
for x in cuser:
    print(' ',x.title())

pets = ['cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
for pet in pets:
    print(pet.title(),end = ' ')

while 'cat' in pets:
    pets.remove('cat')

print()
for pet in pets:
    print(pet.title())

poll = {}

pole = True
while pole:
    name = input('What is your name? ')
    resp = input('Where do you live? ')
    poll[name] = resp
    rept = input('Someone to respond? ')
    
    if rept == 'no':
        pole = False
print(poll)        
for name, resp in poll.items():
    print(name.title(),'lives in',resp)

count = 0
number = 9999
while number > 1:
    # divide number by 3
    number /= 3
    # increase count
    count += 1
print('Total iteration required', count)  

number = int(input('Enter b/w 1 and 100 '))

while number > 1 and number < 100:
    print('Given',number, 'is correct')
    number = int(input('Enter b/w 100 and 500 '))
else:
    print('Given',number,'is incorrect')

#how to break this loop?

x = int(input('Number? '))
while x > 0:

    if x % 2 == 0:
        print(x,'>>> even')
    else:
        print(x,'>>> odd')
    x -= 1
#else:
#   print('lakh di laanet')


name = ''
size = len(name)
x = 0
while x < size:
    if name[x].isdecimal():
        x += 1
        continue
    else:
        print(name[x],end = '')
        x += 1

#ABCD

name = 'Jessay1784Pinkman'
size = len(name) #5
x = -1 #-1
while x < size - 1: # x = 3, check = 4
    x += 1 # x = 3
    if not name[x].isalpha():
        continue
    print(name[x], end='')

x = 1
y = 10
while x < y:
    z = 0
    while z < x:
        print('*', end = ' ')
        z = z+1
    print()
    x = x+1

a = 3-y
b = 1
while a < b:
    c = a
    while c < b:
        print('*',end = ' ')
        c = c+1
    print()
    a = a+1

x = 1
y = 9
while x < y:
    for z in range(x):
        print('*', end = ' ')
    print()
    x = x+1

a = 1
b = y
while a < b:
    for c in range(b-a-1):
        print('*',end = ' ')
    print()
    a = a+1

x = 1
y = 7
while x < y:
    for z in range(y-x-1):
        print(' ', end = ' ')
    for z in range(x):
        print('*',end = ' ')
    print()
    x = x+1

a = 1
b = y
while a < b:
    for c in range(a):
        print(' ',end = ' ')
    for c in range (b-a-1):
        print('*',end = ' ')
    print()
    a = a+1 
'''
x = 1
y = int(input('Stars: '))+1

while x < y:
    n = 0
    while n < y-x-1:
        print(' ', end = ' ')
        n = n+1
    m = 0
    while m < x:
        print('*',end = ' ')
        m = m+1
    print()
    x = x+1

a = 1
b = y-1

while a < b:
    m = 0
    while m < a:
        print(' ', end = ' ')
        m = m+1
    n = 0
    while n < b-a:
        print('*',end = ' ')
        n = n+1

    print()
    a = a+1
'''
for x in range (6):
    for y in range (x):
        print(y+1, end = ' ')
    print()

x = int(input('Enter a value: '))
y = []
for n in range(x+1):
    y.append(n)
print()
print('The sum is',sum(y))

x = 0
a = int(input('Number: '))
for num in range(a+1):
    x = x+num
print(x)

for num in range (1,11):
    print(num*2)

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num%5==0 and num <= 150:
        print(num)
    if num > 500:
        break

numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num > 500:
        break
    elif num > 150:
        continue
    elif num % 5 == 0:
        print(num)

num = 75869
val = 0
while num != 0:
    num = num // 10
    val = val + 1
print(val)

x = 7
for num in range(x):
    for val in range (x-num):
        print(x-val,end = ' ')
    print()

a = [10, 20, 30, 40, 50]
b = []
   
for x in range(len(a)):
    b.append(a[len(b)-x-1])
print(b)   
print(a[::-1])

x = len(a)
for i in range(x-1,-1,-1):
    print(a[i])

for x in range(-1,-11,-1):
    print(x,end=' ')

for i in range(5):
    print(i)
else:
    print('Done!')

x = 0
y = 1
for num in range(int(input('Range: '))):
    print(x,end = ' ')
    z = x+y
    x = y
    y = z

x = int(input('Number: '))
y = 1
for a in range(1,x+1):
    y = y*a
print(y)

number = 765421
num = str(number)
for i in range(len(num)):
    print(num[len(num)-i-1],end='')

mlist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(len(mlist)):
    if i % 2 != 0:
        print(mlist[i],end=' ')
print()
for x in mlist[1::2]:
    print(x,end = ' ')

n = 5
y = 5
x = y
num = []
for i in range(n):
    num.append(y)
    y = y*10+x
for x in num:
    print(x,end=' ')
print()
print('The sum is:',sum(num))

name = ''
while name != 'quit':
    name = input('Name: ')
    if name == 'quit':
        break
    else:
        print('Your name is: ',name.title())
print('Thank you')

while True:
    name = input('Your Name: ')
    if name != 'Joe':
        continue
    print('Hello,',name,'What is your pass?')
    passd = input('Your Password: ')
    if passd == 'fish':
        break
print('Access Granted')

print('My name is')
for i in range(5):
    print('Jimmy Five Times ('+str(i)+')')  

import random
secret = random.randint(1,10)
atm = 4
print('You have '+str(atm)+' attempts')
for x in range(atm):
    guess = int(input('Your Number: '))
    if guess > secret:
        print('Your guess is high')
        print('You have '+str(atm-x-1)+' more attempts')
    elif guess < secret:
        print('Your guess is low')
        print('You have '+str(atm-x-1)+' more attempts')
    else:
        break
if guess == secret:
    print('The Correct Answer is',secret)
    print('You have guessed it in '+ str(x+1) +' attempts')
else:
    print('Hard luck, try again')
if x+1 == 1:
    print('Your are a genious')
elif guess != secret and x+1 == atm:
    print('Lakh di laanet ae kaka')
elif guess == secret and x+1 == atm:
    print('Ja pai kamm kar')

def spam(x):
    try:
        maz = 42/x
        return maz
    except ZeroDivisionError:
        print()
print(spam(1))
print(spam(2))
print(spam(0))
print(spam(3))
 '''       
    
    