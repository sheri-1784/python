from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = 0
        
root --> root of the tree.

def treeTraversal(root):
    if root == None:
        return
    print(root.data)
    treeTraversal(root.left)
    treeTraversal(root.right)


    

        
        
        