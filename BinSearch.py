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
        
def addNum(root, meta):
    if root == None:
        root = Node(meta)
    else:
        if meta < root.data:
            if root.left == None:
                root.left = Node(meta)
            else:
                addNum(root.left, meta) 
        elif meta > root.data:
            if root.right == None:
                root.right = Node(meta)
            else:
                addNum(root.right, meta)
            
            
def printTree(root):
    if root == None:
        return
    printTree(root.left)
    print(root.data, end=' ')
    printTree(root.right)

        

def findNum(node, num):
    if node == None:
        print('Num not found')
        return
    if node.data == num:
        print('Number found:',num)
    elif num < node.data:
        findNum(node.left, num)
    elif num >= node.data: 
        findNum(node.right, num)

    
def maxDepth(root):
    if root == None:
        return -1
    ldepth = maxDepth(root.left)
    rdepth = maxDepth(root.right)
    
    if ldepth > rdepth:
        return ldepth + 1
    return rdepth + 1

            
root = Node(0)
addNum(root,3)
addNum(root,1)
addNum(root,2)
addNum(root,5)
addNum(root,4)
addNum(root,7)
addNum(root,6)
addNum(root,8)
addNum(root,9)

printTree(root)
print()
findNum(root, 10)
d = maxDepth(root)
print('Tree Depth:',d)

      
                
            