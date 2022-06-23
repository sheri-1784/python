from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def prinTree(root):
    if root == None:
        return
    #print(root.data,end=' ')
    prinTree(root.left)
    #print(root.data,end=' ')
    prinTree(root.right)
    print(root.data,end=' ')

count = [0]
def nthNode(root, n):
    if root == None:
        return
    if count[0] <= n:
        
        nthNode(root.left, n)
        nthNode(root.right, n)
        
        count[0] += 1
        
        if count[0] == n:
            print(str(n)+'th Node:',root.data)
            
def printLevel(root):
    h = height(root)
    for i in range(1,h+1):
        pCurrent(root, i)

def pCurrent(root, i):
    if root == None:
        return
    if i == 1:
        print(root.data,end=' ')
    else:
        pCurrent(root.left, i-1)
        pCurrent(root.right, i-1)
'''
#
00 0
01 1
10 2
11 3

010 +2
110 -2

011 +3 (MAX) ==> + inf
111 -3 (MIN) ==> - inf


0(31-bit 111s)  ==> + inf
1(31-bit 111s) ==> - inf


# { - 100 to 100, 4-bytes --> MIN = -2^32-1 --> MAX = 2^32 - 1}
# 
# 1 ( - max to max). Int = 32 bit. (4 bytes) 
    3 - root ===> min(min (1, 2), 3) --> 1
  1   2 
x  x x  x

min(node.data, +inf) --> node.data.

    1  --> min --> 1
   x x 

       1  --> min --> 1
   +inf +inf 


         1  ---> 1
  INT_MAX  INT_MAX  ---> min(min(INT_MAX, INT_MAX), 1)


         2  ---> 2
  INT_MAX  INT_MAX  ---> min(min(INT_MAX, INT_MAX), 2)
'''
def plus(root):
    if root == None:
        return 0
    return (root.data 
        + plus(root.left)
        + plus(root.right))

def sumleft(root):
    if root == None:
        return 0
    return (root.data 
        + plus(root.left))

def sumright(root):
    if root == None:
        return 0
    return (root.data 
        + plus(root.right))

def findBig(root):
    if root == None:
        return
    lsum = sumleft(root)
    rsum = sumright(root)
    
    if lsum > rsum:
        print('LeftSum:',lsum)
    else:
        print('RightSum:',rsum)
'''
def main():
    summ = takeTwoInputsAndReturnSUm()
    print(summ)
    
def takeTwoInputsAndReturnSUm():
    a = input()
    b = input()
    recursive(root.left, i-1)
    sum(a, b)
    return sumOftwoNubers



f(a) summ()
f(b)
f(main)


def summ (a, b):
    return a+b

def findMin(root):
    h = height(root)
    y = []
    for i in range(h):
        y.append(pen(root, i))
           # pen(root=1, i=0) ===> 1
           # pen(root=1, i=1) ===> 1

    print(y)

    1 -- >0 
   3  4  --> 1

pen(root=1, i=0) ===> 1
pen(root=1, i=0) ===> 3
                 ---> 4
i=2

    [4,5,6,7]
[4,5]  [6,7]
                pen(root = 1, i=1) x = 2, y = 3, return [2, 3]            
            /  2                     \ 3
        pen(root.left = 2, i=0)     pen(root.right = 3, i=0) 

'''
def height(root):
    if root == None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    
    if lh > rh:
        return lh+1
    return rh + 1

def findNum(root, x):
    if root == None:
        return
    findNum(root.left, x)
    if root.data == x:
        print('Found Num:',x)
    findNum(root.right, x)
          
def findLevel(root, x):
    return _findLevel(root,x,1)

def _findLevel(root, x, y):
    if root == None:
        return 0
    if root.data == x:
        return y
    dlevel = _findLevel(root.left,x,y+1)
    if dlevel != 0:
        return dlevel
    dlevel = _findLevel(root.right,x,y+1)
    return dlevel

def findMax(root):
    if root == None:
        return float('-inf')
    dx = root.data
    ldx = findMax(root.left)
    rdx = findMax(root.right)
    
    if ldx > dx:
        dx = ldx
    if rdx > dx:
        dx = rdx
    return dx

def findMin(root):
    if root == None:
        return float('inf')
    dx = root.data
    ldx = findMin(root.left)
    rdx = findMin(root.right)
    
    if ldx < dx:
        dx = ldx
    if rdx < dx:
        dx = rdx
    return dx


    
        
    
    
    
root = Node(1)

node2 = Node(2)
node3 = Node(3)
root.left = node2
root.right = node3

node4 = Node(4)
node5 = Node(5)
node2.left = node4
node2.right = node5

node6 = Node(6)
node7 = Node(7)
node3.left = node6
node3.right = node7

prinTree(root)
print()
#findMin(root)
print(findLevel(root, 4))

m = findMax(root)
for i in range(1,m+1):
    level = findLevel(root, i)
    if level != 0:
        print('Level of',i,'is',level)
    else:
        print('>>>',i,'not in tree')
        
print('Tree Min:',findMin(root))