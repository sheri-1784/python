from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkList:
    def __init__(self):
        self.head = None
        
    def addNumber(self, num):
        node = Node(num)
        if self.head == None:
            self.head = node
            #return
        else:
            node.next = self.head
            self.head = node
        
    def addLast(self, num):
        node = Node(num)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

    
    def printList(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next
    
    


x = LinkList()

#n1 = x.addNumber(4)
#n2 = x.addNumber(6)
#n3 = x.addNumber(8)
#n4 = x.addNumber(9)
n1 = x.addLast(4)

x.printList()
#print('---')
'''
y = LinkList()

n1 = y.addLast('A')
n2 = y.addLast('B')
n3 = y.addLast('C')
n4 = y.addLast('D')
n5 = y.addLast('E')

y.printList()
'''   
    