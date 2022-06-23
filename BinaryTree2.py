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
        
def printTree(root):
    if root == None:
        return
    #print(root.data,end=' ')
    printTree(root.left)
    print(root.data,end=' ')
    printTree(root.right)
    #print(root.data,end=' ')
    
count = 0 #why like this? :)
def nthNode(root, n): ## 27, 3 --. #1, 4
    #count = 0
    if root == None: 
        return
    if count <= n: #0 < 3 #whats wrong with While?
        nthNode(root.left, n) # nthNode(27.left,3)
        nthNode(root.right, n) #nthNode(35, 3)
        count += 1 # 4
        #print('left done')
        if count == n:
            print('Nth Node:', root.data) #9
        #print('right done')
        #return

#    10
#   /  \
# None  None       
    
def maxDepth(root): #10
    if root == None: #
        return -1
    else:
        ldepth = maxDepth(root.left) # 10.left = None
        # ldepth = -1
        rdepth = maxDepth(root.right)
        # rdepth = -1
        
        if ldepth > rdepth:
            return ldepth+1
        return ldepth+1
        
'''##    27
##  None  None    
    
depth_global = -1

def maxDepth(root):
    helper(root, -1) # 27, -1
    return depth_global

def helper(root, depth): # (27, -1)
    if(root == None):
        return
    curr_depth = depth + 1 # curr_depth = 0
    if curr_depth > depth_global: 
        depth_global = curr_depth # global_depth = 0
            
    helper(root.left, curr_depth)
    helper(root.right, curr_depth)    
'''    

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

#node8 = Node(8)
#node9 = Node(9)
#node4.left = node8
#node4.right = node9
    
printTree(root)
print()
depth = maxDepth(root)
print('Tree depth:',depth)

nthNode(root,3)