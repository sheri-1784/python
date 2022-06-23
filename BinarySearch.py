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
        
    def addNum(self, meta):
        if self.data == None:
            self.data = Node(meta)
        else:
            if meta < self.data:
                if self.left == None:
                    self.left = Node(meta)
                else:
                    self.left.addNum(meta) 
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
        
    def search(self, num):
        if root == None:
            return
        if self.data == num:
            print('Number found')
        else: 
            if self.data > num:
                self.left.search(num)
            self.right.search(num)

            


root = Node(5)
root.addNum(3)
root.addNum(1)
root.addNum(2)
root.addNum(5)
root.addNum(4)
root.addNum(7)
root.addNum(6)
root.addNum(8)
root.addNum(9)

root.printTree()
print()
root.search(6)
                
            