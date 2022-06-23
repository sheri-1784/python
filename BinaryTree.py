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
        
    def addNum(self, meta): #imp by bredth
        if self.data == None:
            self.data = Node(meta) #node or just data?
        else:
            if meta < self.data:
                if self.left == None:
                    self.left = Node(meta)
                else:
                    self.left.addNum(meta) # 3.add(1)
            elif meta > self.data:
                if self.right == None:
                    self.right = Node(meta)
                else:
                    self.right.addNum(meta)
            
            
    def printTree(self):
        #print(self.data, end=' ')
        if self.left != None:
            self.left.printTree()
        print(self.data,end=' ')
        if self.right != None:
            self.right.printTree()
        #print(self.data, end=' ')
        
#        5
#      3   
#    1   4
#      2 

root = Node(5)
root.addNum(3)
root.addNum(1)
root.addNum(2)
root.addNum(5)
root.addNum(4)
root.addNum(7)


#        1, 2, 3

#         2
#       1   3
#      1 2 3
      
#      3
#     2
#    1
#    1 2 3
      
#    1
#     2
#      3
#   1 2 3   

root.printTree()

print()
root = Node(5)

node2 = Node(3)
node4 = Node(4)
root.left = node2
root.right = node4

node1 = Node(1)
node5 = Node(2)
node2.left = node1
node2.right = node5

node6 = Node(6)
node7 = Node(7)
node4.left = node6
node4.right = node7

def printTee(root):
    if root == None:
        return
    #print(root.data, end = ' ')
    printTee(root.left)
    print(root.data, end = ' ')
    printTee(root.right)
    #print(root.data, end = ' ')

printTee(root)

                
            