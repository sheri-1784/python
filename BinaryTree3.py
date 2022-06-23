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

def printTree(root):  # root == B    
    if root == None:
        return
    #print(root.data,end=' ')
    printTree(root.left)
    print(root.data,end=' ')
    printTree(root.right)
    return 
    
def maxDepth(root):
    if root == None:
        return -1
    ldepth = maxDepth(root.left)
    rdepth = maxDepth(root.right)

    if ldepth > rdepth:
        return ldepth+1
    return ldepth+1

def levelPrint(root):
    h = height(root)
    for i in range(1,h+1):
        printCurrent(root, i)
        
def height(root):
    if root == None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    
    if lh > rh:
        return lh+1
    return rh+1

def printCurrent(root, level):
    if root == None or level == 0:
        return
    if level == 1:
        print(root.data,end =' ')
    printCurrent(root.left, level-1)
    printCurrent(root.right, level-1)



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

printTree(root)
print()
print(maxDepth(root))
levelPrint(root)