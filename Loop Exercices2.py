from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()
'''   
n = 6
for x in range(n):
    for i in range(n-x-1):
        print(' ',end=' ')
    for i in range(x+1):
        print('*',end=' ')
    print()
    
for x in range(n-1):
    for i in range(x+1):
        print(' ',end=' ')
    for i in range(n-x-1):
        print('*',end=' ')

for x in range(5):
    for i in range(x+1):
        print(i+1,end=' ')
    print()
    
num = 10
dum = []
for x in range(num+1):
    dum.append(x)
print(sum(dum))

print(sum(list(range(num+1))))
print(sum(range(num+1)))

m = 0
for x in range(num+1):
    m = m+x
print(m)

for i in range(1,11):
    m = 2*i
    print(m)

number = [12, 75, 150, 180, 145, 525, 50]  

for i in number:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i,end=' ')

for x in range(5):
    for i in range(5-x):
        print(5-i-x,end=' ')
    print()

num = [10, 20, 30, 40, 50]

for i in range(len(num)-1,-1,-1):
    print(num[i])

for i in range (-10,0,1):
    print(i)

for i in range(5):
    print(i)
print('Done')

x = 25
y = 50   

for i in range(x,y):
    for a in range(2,i):
        if i % a == 0:
            break
    else:
        print(i)

x = 0
y = 1

for i in range(11):
    print(x,end=' ')
    a = x+y
    x = y
    y = a
print()

x = 1
for i in range(1,6):
    x = x*i
print(x)

a = 76542
b = str(a)

for i in range(len(b)-1,-1,-1):
    print(b[i],end='')
print()    
m = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(len(m)):
    if i % 2 != 0:
        print(m[i])

x = 2
y = 0
n = 5
for i in range(n):
    y = y+x
    x = x*10+2
print(y)

x = 0
n = 10
while x < n:
    x = x+1
    if x % 2 == 0:
        continue
    else:
        print(x,end=' ')

x = ['kaka', 'mama', 'jama']   
x.append('lama')
x.insert(1,'dada')
print(x)
y = []

while x:
    y.append(x.pop())
    print(y)

poll = {}

true = True
while true:
    name = input('Name: ')
    city = input('City: ')
    poll[name] = city
    resp = input('Response ')
    
    if resp == 'no':
        break
#print(poll)
print()
for x,y in poll.items():
    print(x,'lives in',y)
   
x = 999999
c = 0

while x > 1:
    x = x/9
    c = c+1
print(c)

name = 'Jessay1784 Pinkman'
x = 0
while x < len(name):
    if not name[x].isalpha():
        x = x+1
        continue
    else:
        print(name[x],end='')
        x = x+1
print()        
name = 'Jessay1784 Pinkman'
x = 0
while x < len(name):
    x = x+1
    if not name[x-1].isalpha():
        continue
    else:
        print(name[x-1],end='')
print()       
name = 'Jessay1784 Pinkman'
x = 0
while x < len(name):
    x = x+1
    if name[x-1].isdecimal():
        continue
    else:
        print(name[x-1],end='')
 '''
x = 0
y = 7
while x <= y:
    z = 0
    while z <= x:
        print('*',end=' ')
        z = z+1
    print()
    x = x+1
    
a = 0
b = y
while a <= b:
    c = 0
    while c <= b-a-1:
        print('*',end=' ')
        c = c+1
    print()
    a = a+1
        
x = 0
while x <= y:
    z = 0
    while z <= y-x-1:
        print(' ',end=' ')
        z = z+1
    v = 0
    while v <= x:
        print('*',end=' ')
        v = v+1
    print()
    x = x+1
    
a = 0
while a <= b:
    c = 0
    while c <= a:
        print(' ',end=' ')
        c = c+1
    d = 0
    while d <= b-a-1:
        print('*',end=' ')
        d = d+1
    print()
    a = a+1   
    
   
    
    
 

    
      
        
    
 
    
    
    
    