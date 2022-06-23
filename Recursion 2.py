from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()

def count(n):
    print(n)
    if n > 0:
        count(n-1)
        print(n)
        
count(4)

'''
def countd(n):
    while n >= 0:
        print(n)
        n = n-1

countd(5)

def fact(n):
    if n == 0:
        return 1
    else:
        return n * (fact(n-1))
    
m = fact(6)
print(m)

def fac(n):
    for i in range(1,n):
        n = n*i
    print(n)

fac(6)

name = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']

def counted(xlist):
    count = 0
    for i in xlist:
        if isinstance(i, list):
            count += counted(i)
        else:
            count += 1
    return count

y = counted(name)
print(y)

#num = [2,3,4,5,6]

def count(m):
    x = 0
    for i in m:
        if i % 2 == 0:
            x += 1
        else:
            x += 1
    return x

y = count(range(110))
print(y)
        
name = ['a',['b','c'],'d',[['e','f',['k',['l','m']]],'g','h'],'j','k']
print(len(name))

def count(items):
    x = 0
    for item in items:
        if isinstance(item,list):
            x = x+count(item)
        else:
            x = x+1
    return x

y = count(name)
print(y)  

def pali(word):
    if len(word) == 0:
        return True
    else:
        return word[0] == word[-1] and pali(word[1:-1])

mds = pali('112211')
print(mds)

import statistics

def sort_and_remove_duplicates():
    remove_duplicate()

def sort(number):
    if len(number) <= 1:
        return number
    else:
        pivot = statistics.median([
            number[0],
            number[len(number)//2],
            number[-1]
            ])

        less, equal, great = (
            [n for n in number if n < pivot],
            [n for n in number if n == pivot],
            [n for n in number if n > pivot]
            )
        return (sort(less) + equal + sort(great))

xyz = [0,2,4,3,5,16,8,9,4,3,115,16,17,8,9,10,44,55,66,6]
m = sort(xyz)
print(m)
print()

list1 = []
for n in range(15):
    val = fib(n)
    list1.append(val)
    
#num = [2,4,4,3,5,6,8,9,4,3,5,6,7,8,9,0,44,55,66,66]
num = [1,2,2,3,3,3,4]

#print(len(num))
#num.sort()

for i in range(len(num)-1):
    #print(num[i],end=' ')
    if i+1 == len(num):
        break    
    elif num[i] != num[i+1] and (i+1) <= (len(num)-1):
        continue
    elif num[i] == num[i+1] and (i+1) <= (len(num)-1):
        num.pop(i)
print(num)

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
        return (sort(less) + equal + sort(great))

#xyz = [2,4,4,3,5,6,8,9,4,3,117,6,7,8,9,0,44,55,66,66]
m = sort(xyz)
print(m)
print()

print(xyz[len(xyz)//2])
import statistics
abc = statistics.median([xyz[0],xyz[len(xyz)//2],xyz[-1]])
print(abc)

#With Average

def sort(number):
    if len(number) <= 1:
        return number
    else:
        pivot = sum(number) / len(number)
        
        # 1, 2, 3, 4, 5, 6, 7, 8, 500, 2000, 4000, 8000
    
        less = [x for x in number if x < pivot]
        equal = [x for x in number if x == pivot]
        great = [x for x in number if x > pivot]
            
        return (sort(less) + equal + sort(great))

xyz = [0,2,4,3,5,6,8,9,4,3]
m = sort(xyz)
print(m)

import statistics

def sort(number):
    if len(number) <= 1:
        return number
    else:
        pivot = statistics.median([
            number[0],
            number[len(number)//2],
            number[-1]
            ])
    
        less = [x for x in number if x < pivot]
        equal = [x for x in number if x == pivot]
        great = [x for x in number if x > pivot]
            
        return (sort(less)+equal+sort(great))

xyz = [0,2,4,3,5,6,8,9,4,3]
m = sort(xyz)
print(m)

#num = [2,4,4,3,5,6,8,9,4,3,5,6,7,8,9,0,44,55,66,66]
num = [1,2,2,3,3,3,4]

next_correct_slot_index = 0
num = [1,2,2,3,3,3,4]


next_correct_slot_index = 1
num = [1,2,2,3,3,3,4]

next_correct_slot_index = 2
num = [1,2,2,3,3,3,4]

next_correct_slot_index = 2
num = [1,2,3,3,3,3,4]

next_correct_slot_index = 3
num = [1,2,3,4,3,3,4]

next_correct_slot_index = 4
#start =0; end = 6

# 2 2 2 2 2 2 2 2 
#num = [1,2,3,3,3,4]
#len = 6
#start=0; end = 5


#print(len(num))
#num.sort()

length = len(num) - 1
for i in range(len(num)-1):
    #print(num[i],end=' ')
    if i == len(num):
        break    
    elif num[i] != num[i+1] and (i+1) <= (len(num)-1):
        continue
    elif num[i] == num[i+1] and (i+1) <= (len(num)-1):
        num.pop(i)
        lenth -= 1
print(num)

#num = [2,4,4,3,5,6,8,9,4,3,5,6,7,8,9,0,44,55,66,66]
num = [1,2,2,2,3,3,3,4,4,5,5]

#print(len(num))
#num.sort()
leng = len(num)-1
for i in range(leng):
    #print(num[i],end=' ')
    if i+1 == leng:
        break    
    elif num[i] == num[i+1] and (i+1) <= leng:
        num.pop(i)
        print(len(num))
        leng = leng-1
print(num)

def rem_dup(num):
    i = 0
    while i < len(num):
        if num[i] != num[i+1]:
            return [num[i]]+[num[i+1]]
        else:
            num.pop(i)
            return rem_dup(num)
    
x = [1,1,2,2,2,3,3,3,4,4,5,5]
y = rem_dup(x)
print(y)

def sum_r(x, y):
    if x == c:
        return y
    else:
        return sum_r(x + 1, y + x)

print(sum_r(1,0))

x = 0
y = 100
for i in range(y):
    x = x+i
print(x)
'''
        
F =#  0 1 1 2 3 5 8 13 21 34 ...
# F(n) = F(n-1) + F(n-2)

n = 2
F(2) = F(1) + F(0)
F(3) = F(2) + F(1)



F(4) = F(3) + F(2)
..
..
F(X) = F(X-1) + F(X-2)


F(n) = (F(n-2) + F(n-3)) + F(n-2)

n-1 = k
F(n-1) = F(n-1-1) + F(n-1-2)
F(n-1) = F(n-2) + F(n- )

                    F(n)
                F(n-1) + F(n-2)
                    
Line/Question: "Given a problem-size of n, standing at root, ask your children nodes, can you solve this problem for me for problem-size= n-(n-1)"
        
        
nth fibonacci =>
n-1th fibnoacci  < nth fibnoacci.

n =  5 3 4 2 1
   smallest-element = 1
    1, f([5 3 4 2])
        smallest-element = 2
        2 , f([3 , 4 , 2])
        3, f(4, 2)



sum of n elements.

F(n) = nth element + F(n-1)
F(n-1) = sum of n - 1






------


Array of size 5= [5, 3,2, 4, 1], size = 5, problem-size = 5
Array of size 4= [ , 3, 2, 4, 1], 5-1 elements, problem-size= 5-1 = 4
Array of size 3= [ ,  , 2, 4, 1], 5-2 elements, problem-size= 5-2 = 3
..

Array of size 2= [ ,  , , 4, 1], problem-size= 2 ==> 4 + sumOf(1)
Array of size 1= [ ,  , , , 1], 5-4 elements, problem-size= 5-4 = 1
    sumOf1Elements = Element
    

sumOf3Elements (2, 4, 1) + 3 ==> sumOf4() + 5 ==> sumOf5()


Sum(n) = A[n] + Sum(n-1), n= 5 
===> Sum(5) = A[5] + Sum(4)
===> Sum(4) = A[4] + Sum(3)
===> Sum(3) = A[3] + Sum(2)
Sum(2) = A[2] + Sum(1)























