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
    def __init__(self):
        self.head = Node('head')
        self.size = 0
        
    def push(self, x):
        node = Node(x)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
        
    def popq(self):
        if self.head.next != None:
            rem = self.head.next
            self.head.next = self.head.next.next
            self.size -= 1
            return rem.data
        
    def printQ(self):
        current = self.head.next
        while current != None:
            print(current.data, end=' ')
            current = current.next
            
class Queue:
    def __init__(self):
        self.head = Node('head')
        self.size = 0
        
    def push(self, x):
        node = Node(x)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
        
    def pop(self):
        current = self.head.next
        previous = None
        while current != None:
            if current.next == None:
                self.head.next = None
                self.size -= 1
                return current.data
            else:
                previous = current
                current = current.next
                if current.next == None:
                    previous.next = current.next
                    self.size -= 1
                    return current.data

    def getSize(self):
        return self.size
        
    def peek(self):
        current = self.head.next
        while current != None:
            if current.next == None:
                return current.data
            current = current.next

        
    def printQ(self):
        current = self.head.next
        while current != None:
            print(current.data, end=' ')
            current = current.next



q = Queue()
q.push(1)
q.push(2)
q.push(3)
#q.push(4)
#q.push(5)
#q.push(6)

q.printQ()
print()
print('Size:',q.getSize())

print(q.pop())
print(q.pop())
print(q.pop())

q.printQ()
print()
print('Size:',q.getSize())
  
        


