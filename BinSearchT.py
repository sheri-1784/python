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
        
def addNode(root, x):
    if root == None:
        root = Node(x)
    else:
        if x < root.data:
            if root.left == None:
                root.left = Node(x)
            else:
                addNode(root.left, x)
        elif x > root.data:
            if root.right == None:
                root.right = Node(x)
            else:
                addNode(root.right, x) 


def prinTree(root):
    if root  == None:
        return
    prinTree(root.left)
    print(root.data, end=' ')
    prinTree(root.right)
    
def findLevel(root):
    if root == None:
        return 0
    ll = findLevel(root.left)
    rl = findLevel(root.right)
    
    if ll > rl:
        return ll+1
    else:
        return rl+1

def findNum(root, x):
    if root == None:
        return
    if root.data == x:
        print('Number', x,'found')
    else:
        findNum(root.left, x)
        findNum(root.right,x)

def findMinMax(root):
    print('Min Value:',findMin(root))
    print('Max Value:',findMax(root))
    return

def findMin(root):
    if root == None:
        return
    if root.left == None:
        return root.data
    else:
        x = findMin(root.left)
        return x

def findMax(root):
    if root == None:
        return    
    if root.right == None:
        return root.data
    else:
        y = findMax(root.right)
        return y
    
def levelOrder(root):
    h = findLevel(root)
    for i in range(h):
        prCurrent(root,i)
        
def prCurrent(root,i):
    if root == None:
        return
    if i == 0:
        print(root.data,end=' ')
    prCurrent(root.left,i-1)
    prCurrent(root.right,i-1)   
    
def findLevel(root,x):
    return ifindLevel(root,x,1)
    
def ifindLevel(root,x,i):
    if root == None:
        return 0
    if root.data == x:
        return i
    a = ifindLevel(root.left,x,i+1)
    if a != 0:
        return a
    a = ifindLevel(root.right,x,i+1)
    return a
  
    

root = Node(6)
addNode(root,2)
addNode(root,4)
addNode(root,1)
addNode(root,3)
addNode(root,5)
addNode(root,7)
addNode(root,8)
#addNode(root,9)

prinTree(root)
print()

m = findMax(root)
for i in range(1,m+1):
    level = findLevel(root,i)
    if level != 0:
        print('Level of',i,'is',level)
    else:
        print('Node',i,'not found')             