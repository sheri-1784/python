from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()

'''
def funct:
    # base case.
    # DO STUFF BEFORE CALLING RECURSION
        # CALL RECRUSIVE METHOD
    # DO STUFF AFTER RECURSION
    
def a([1, 2]):
    ----
    a([1])
    ---

def a([1]):
    ----
    a([])
    ------

def a([]):
    ----
    return x
    
  
def count(x):
    print(x)
    if x == 0:
        return 445
    else:
        ret = count(x-1) 
        print(ret) # 1
        return ret + 1
    
count(5)
     
            count(5)
            count (4)
            count (3)
            count (2)
            count (1)
            
            
FUNCTION CALL STACK.

5 
    4 
        3 
            2 
                1 
                    0
                1
            2
        3
    4
5

            
count(0)
count(1)
count(2)
count(3)
count(4)
count(5)

def fab(x):
    if x <= 1:
        return x+1
    else:
        return fab(x-1)+fab(x-2) 
    
num = 0

print(fab(num))

for i in range(num+1):
    print(fab(i),end=' ')
print()    

'''    
def fact(x):
    if x == 0:
        return 1
    else:
        return x*(fact(x-1))
    
fact(5)
'''
x = 3
y = 4

def rep_cat(x,y):
    return str(x)*10+str(y)*4

print(rep_cat(x,y))

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def div(x,y):
    return x / y

def mul(x,y):
    return x * y

def calc(a,x,y):
    return a(x,y)

res1 = calc(add,12,4)
res2 = calc(sub,12,4)
res3 = int(calc(div,12,4))
res4 = calc(mul,12,4)

print(res1,res2,res3,res4)

def calc(a,x,y):
    return a(x,y)

result = calc(lambda x,y: x+y,4,5)
print(result)

# Python program to demonstrate
# lambda functions


x ="GeeksforGeeks"

# lambda gets pass to print
(lambda x : print(x))(x)

def cube(x):
    return x*x*x

print(lambda x: x*x*x,4)

print(cube(5))
#print(lambda_c(5))

tables = [lambda x=x: x*10 for x in range(1,10)]

for table in tables:
	print(table())
    
add = lambda a,b,c: a*b**c
print(add(1,2,3))

res = lambda a,b,c: a*b**c
print(res(1,2,3))

List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]

# Sort each sublist
sortList = lambda x: (sorted(i) for i in x)

# Get the second largest element
secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
res = secondLargest(List, sortList)

print(res)

nlist = [1,2,3,4,5,6]

dlist = list(map(lambda x: x**2, nlist))
clist = list(filter(lambda n: n>4, nlist))
#for n in dlist:
#    clist.append(n)
#print(clist)

print(dlist)
print(clist)

n = 50
num_list = [10, 4, 23, 6, 18, 27, 47]
found = False  # This bool will become true once a pair is found

for n1 in num_list:
    for n2 in num_list:
        if(n1 + n2 == n):
            found = True  # Set found to True
            break  # Break inner loop if a pair is found
    if found == True:
        print(n1, n2) # Print the pair
        break  # Break outer loop if a pair is found
'''