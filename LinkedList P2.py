from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkList:
    def __init__(self):
        self.head = None
        
    def printList(self):
        current = self.head
        if current == None:
            print('Empty List')
        else:
            while current != None:
                print(current.data, end=' ')
                current = current.next
            print()
    
    def lengList(self):
        current = self.head
        if current == None:
            print('Empty List')
        else:
            length = 0
            while current != None:
                current = current.next
                length += 1
            print('length:',length)
            
    def addNum123(self, num):
        node = Node(num)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
            
    def addNum321(self, num):
        node = Node(num)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            node.next = current
            self.head = node
            
    def addAfter(self, a, b): #add 'b' after 'a'
        node = Node(b)
        current = self.head
        if current == None:
            self.head = node
        else:
            current = self.head
            while current != None and current.data != a:
                current = current.next
            node.next = current.next
            current.next = node
            return
    
    def replaceNum(self, a, b): #rep 'a' with 'b'
        node = Node(b)
        current = self.head
        if current == None:
            self.head = node
        else:
            #current = self.head
            while current != None and current.data != a:
                current = current.next
            current.data = b
                 
    def delNumEq(self,num):
        if self.head != None and self.head.data == num:
            self.head = self.head.next
        else:
            prev = None
            current = self.head
            while current != None and current.data != num:
                prev = current
                current = current.next
            if current != None:
                prev.next = current.next

    def delAfter(self, a): #del after 'a'
        current = self.head
        if current == None:
            print('Empty List')
        elif current.data == a and current.next == None:
            print('Nothing to del')
        elif current.data == a and current.next != None:
            self.head.next = current.next.next
        else:
            current = self.head
            prev = None
            while current != None and current.data != a:
                prev = current
                current = current.next
            if current != None:
                prev.next = current.next
                
    def delNumAt(self, n): #need to add length to avoid error
        current = self.head
        prev = None
        if current == None:
            print('ja kam kar')
        elif current != None and n == 1:
            self.head = self.head.next
        else:
            for i in range(n-1):
                prev = current
                current = current.next
            prev.next = current.next  
            
    def findNth(self, n):
        current = self.head
        if current == None:
            print('ja kam kar')
        else:
            for i in range(n-1):
                current = current.next
            print(current.data)
            
    def revList(self):
        previous = None
        current = self.head
        forward = None
        if current == None:
            return
        while current != None:
            forward = current.next
            current.next = previous
            previous = current
            current = forward
        self.head = previous
        
    def nthFromLast(self, n):
        current = self.head
        length = 0
        while current != None:
            current = current.next
            length = length + 1
            
        if n > length or n < 1:
            print('kkkkkkk')
        else:
            current = self.head
            for i in range(length - n):
                current = current.next
            print(current.data)
    
    def kthFromLast(self, k):
        temp = self.head
        length = 0
        while temp != None:
            temp = temp.next
            length = length + 1
        
        if k > length or k < 1:
            print('kkkkkk')
        else:
            temp = self.head
            pine = self.head
            for i in range(k):
                pine = pine.next
            while pine != None:
                temp = temp.next
                pine = pine.next
            print(temp.data)
                    

x = LinkList()

x.addNum123(1)
x.addNum123(2)
x.addNum123(3)
x.addNum123(4)
x.addNum123(5)
x.addNum123(6)
x.addNum123(7)
x.addNum123(8)

x.printList()

print('---------------')

x.replaceNum(9, 12)
x.printList()