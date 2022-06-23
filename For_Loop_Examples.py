from time import sleep

def cls():
    print("\033[2J\033[;H", end='')
    sleep(0.1)

cls()

'''
for num in range(3):
    print(num+1,end=' ')
'''    
for val in range(5):
    for duc in range(val+1):
        print(duc+1,end=' ')
    print()
'''   
r = 5
start: 1
stop: row+1 (range never include stop number in result)
step: 1
run loop 5 times
for i in range(1, r + 1, 1): # Run inner loop i+1 times
    for j in range(1, i + 1):
        print(j, end=' ')    # empty line after each row
    print("")

num  = int(input('Enter a value: '))
number = []
for lex in range(num+1):
    number.append(lex)
print()
print('The sum is',sum(number))

# s: store sum of all numbers
s = 0
n = int(input("Enter number "))
# run loop n times
# stop: n+1 (because range never include stop number in result)
for i in range(1, n + 1, 1):
    # add current number to sum variable
    s += i
print()
print("Sum is: ",s)

num  = int(input('Enter a value: '))
number = list(range(num+1))
print(sum(number))

num = int(input('Enter a value: '))
dum = sum(range(num+1))
print(dum)

for num in range(11):
    print(num*2)

number = [12, 75, 150, 180, 145, 525, 50]
for num in number:
    if (num % 5)==0 and num<=150:
        print(num)
print()

number = [12, 75, 150, 180, 145, 525, 50]
for num in number:
    if num >500:
        break
    elif (num % 5)== 0 and num <=150:
        print(num)

numbers = [12, 75, 150, 180, 145, 525, 50]
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item % 5 == 0:
        print(item)


for val in range(5):
    for num in range(5-val,0,-1):
        print(num,end=' ')
    print()

list1 = [10, 20, 30, 40, 50]
list1.reverse()
for num in list1:
    print(num)
    
for num in range(6,0,-1):
    print(num,end=' ')

    
number = [10, 20, 30, 40, 50]
for x in range(len(number)):
    print(number[len(number)-x-1])
    
number = list(range(1,11))
for x in range(len(number)):
    print(number[len(number)-x-1],end=' ')
    
print()
list1 = [10, 20, 30, 40, 50]
size = len(list1) - 1
for i in range(size, -1, -1):
    print(list1[i])

for val in range(10):
    print(val-10)

for num in range(-10,0):
    print(num)

for num in range(25,50):
    if num % 2 != 0:
        print(num)

print()
number = []
for num in range(25, 50):
    for i in range(2, num): #nai samjh aaya tutt paina
        if (num % i) == 0:
            break
    else:
        number.append(num)
print(number)

num1 = 0
num2 = 1
for num in range(10):
   print(num1,end=' ') #nai samjh aaya haramda
   res = num1+num2
   num1 = num2
   num2 = res

num = int(input('Add your number: '))
fact = 1
for val in range(1,num+1):
    fact = fact*val
print(fact)

for num in range(6):
    for val in range(num+1):
        print('*',end=' ')
    print()
for num in range(6):
    for val in range (5-num):
        print('*',end=' ')
    print()
    
for bac in range(6):
    for val in range(5-bac):
        print(' ',end=' ')   
    for duc in range(bac+1):
        print('* ',end='')
    print()

dum = 15
for num in range(dum):
    for val in range(num+1):
        print('*',end=' ')
    print()
for num in range(dum):
    for val in range(dum-num-1):
        print('*',end=' ')
    print()

a = 9
for x in range(a):
    for b in range(a-x-1):
        print(' ',end = ' ')
    for c in range(x+1):
        print('*',end = ' ')
    print()
    
for x in range(a):
    for b in range(x+1):
        print(' ',end = ' ')
    for c in range (a-x-1):
        print('*',end = ' ')
    print()
'''