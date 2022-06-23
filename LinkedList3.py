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
        while current:
            print(current.data, end=' ')
            current = current.next
            
    def length(self):
        length = 0
        current = self.head
        while current:
            current = current.next
            length += 1
        return length
        
    
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
            node.next = self.head
            self.head = node
            
    def addAfter(self, a, b): #add b after a
        if self.head == None:
            return
        else:
            node = Node(b)
            current = self.head
            while current and current.data != a:
                current = current.next
            else:
                node.next = current.next
                current.next = node
    
    def repLace(self, a, b): #replace a with b
        if self.head == None:
            return
        else:
            node = Node(b)
            current = self.head
            previous = None
            if current and current.data == a:
                node.next = current.next
                self.head = node
            else:
                while current and current.data != a:
                    previous = current
                    current = current.next
                else:
                    node.next = current.next
                    previous.next = node

    def replace(self, a, b): #replace a with b
        node = Node(b)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current and current.data != a:
                current = current.next
            current.data = b
    
    def delNum(self, a):
        if self.head == None:
            return
        elif self.head.data == a:
            self.head = self.head.next
        else:
            previous = None
            current = self.head
            while current and current.data != a:
                previous = current
                current = current.next
            previous.next = current.next

    def delAfter(self, num):
        current = self.head
        while current and current.data != num:
            current = current.next
        else:
            if current.next == None:
                print('Dunald Lu')
            else:
                current.next = current.next.next
   
    def delAtIndex(self, n):
        current = self.head
        length = 0
        while current:
            current = current.next
            length = length+1
        
        current = self.head
        previous = None
        if current and 0 < n <= length:
            if n == 1:
                self.head = self.head.next
            else:
                for i in range(n-1):
                    previous = current
                    current = current.next
                previous.next = current.next
                
    def findNth(self, n):
        current = self.head
        length = 0
        while current:
            current = current.next
            length = length+1
        
        current = self.head
        if current and 0 < n <= length:
            for i in range(n-1):
                current = current.next
            print('Nth Node:',current.data)
    
    def printStars():
        for i in range(2):
            for j in range(3);:
                print("*")
            print("\n")
    
     i = 0
         j = 0
            *
        j = 1
            **
        j = 2
           ***
   i = 1
       j = 0
           *
      j = 1
          **
      J = 2 
          ***
          
***
***
              
    
    
    
    
    def nthFromLast(self, n):
        current = self.head
        length = 0
        while current:
            current = current.next
            length = length+1
            
        current = self.head
        # n = 2, length =10
        # current 10 -2 = 8/9

        # 1 --> 2 --> 3 --> 4 --> 5 --> null
#                         curr
        #
        # length = 5, n = 10
        #if n > 0 && n < length:
            
            
        while (current != null){
            for(i=0; i < 3; i + = 1){
                current  = current.next        
            }
        }
        while current:
               current = current.next
               if current.data = xyz:
                   do xyz

        print(current.data)
        
    def kthFromLast(self, k):
        current = self.head
        length = 0
        while current:
            current = current.next
            length += 1

        current = self.head
        forward = self.head
        
        if current and 0 < k <= length:
            for i in range(k):
                forward = forward.next
            while forward:
                forward = forward.next
                current = current.next
            print(current.data)

    def revPrint(self, temp):
        if temp:
            self.revPrint(temp.next)
            print(temp.data,end=' ')
        else:
            return

    def revList(self):
        previous = None
        current = self.head
        forward = None
        while current:
            forward = current.next
            current.next = previous
            previous = current
            current = forward
        self.head = previous
            





x = LinkList()
x.addNum123(1)
x.addNum123(2)
x.addNum123(3)
x.addNum123(4)
x.addNum123(5)
x.addNum123(6)


x.printList()
print()
x.revList()
x.printList()            
            
            
            
            
            
            