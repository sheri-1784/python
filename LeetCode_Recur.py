from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()

'''
def fabNumb(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:        
        x = fabNumb(n-1) + fabNumb(n-2)
        return x

n = 10
for i in range(n+1):
    print(fabNumb(i),end=' ')
print()

 
def revString(x):
    left = 0
    right = len(x)-1
    while left < right:
        x[left] = x[right]
        x[right] = x[left]
        left = left+1
        right = right-1

print(revString('hello'))
'''

def reverse(string):
    if len(string) <= 1:
        return
    x = string[::-1]
    return x


def rev(x):
    if len(x) == 0:
        return
    temp = x[0]
    print(temp,end='')
    rev(x[1:])
    print(temp, end='')

def powerTwo(x):
    i = 0
    while (2**i) < x:
        i = i+1
    if (2**i) == x:
        return True
    return False

print(powerTwo(16))

def PowerTwo(x):
    return Power2(x,0)

def Power2(x,i):
    if (4**i) == x:
        return True
    if (4**i) > x:
        return False
    y = Power2(x,i+1)
    return y

#for i in range(10):
    #print(PowerTwo(4**i))
    
def sumOfN(n):
    if n <= 1:
        return n
    x = n+sumOfN(n-1)
    print(x)
    return x

#sumOfN(5)

def revNum(n):
    return _revNum(n,0)

def _revNum(n,i):
    print(i)
    if n < 1:
        return i
    y = _revNum(n//10, i*10 + n%10)
    return y

#revNum(1234)

def power(n, i):
    if i == 0:
        return 1
    y = n * power(n, i-1)
    return y

#print(power(4,6))

def arithSum(a,n,i):
    y = []
    for x in range(1,n+1):
        y.append(a+(x-1)*i)
    return y,sum(y)

print(arithSum(3,5,4))

# 3, 7, 11, 15, 19
# a = 3, i = 4, n = 3
# n = 1 --> 3
# n = 2 --> 10



def arithSum1(a,n,i): # n = 0
    if i <= 0 or n <= 0:
        return 0
    y =  arithSum1(a,(n-1),i) #y = f(3,1,4) = 3
    x = y + (a + (n-1)*i) # 3 + (3+1*4) = 10
    return x

print(arithSum1(3,5,4))    

def sumDigit(n):
    if n < 10:
        return n
    x = n % 10
    y = x + sumDigit(n//10)
    return y

#print(sumDigit(55555))

    
    

    
                 