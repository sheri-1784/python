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
        
class binTree:
    def __init__(self):
        self.root = None
      
        
    def addNum(self, meta):
        if self.root == None:
            self.root = Node(meta)
        else:
            if meta < self.data:
                if self.left == None:
                    self.left = Node(meta)
                else:
                    self.left.addNum(meta)
            elif meta > root.data:
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



tree = binTree()
tree.addNum(5)
tree.addNum(3)
tree.addNum(1)
tree.addNum(2)
tree.addNum(6)
tree.addNum(4)
tree.addNum(7)

tree.printTree()