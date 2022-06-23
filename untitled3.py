from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self)
        self.head = Node('head')
        self.size = 0
        
    def push(self, x):
        node = Node(x)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
        
        


