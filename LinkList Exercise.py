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

    def printList(self):
        current = self.head
        while current != None:
            print(current.data,end=' ')
            current = current.next
        print()

    def reversePrint(head):
        if head is None:
            return
        reversePrint(head.next)
        print(head.data)
        
       ## 1 --> 2 --> 3 --> None
    def revPrint(self,current): #Thanks to Google
        current = self.head #Samjh kujj nai aaya
        while current != None:
            self.revPrint(current.next)
            print(current.data,end=' ')
        else:
            return
        
    def revList (self):
        previous = None
        current = self.head
        forward = None
        while current != None:
            forward = current.next
            current.next = previous
            previous = current
            current = forward
        self.head = previous
            
    def counter(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        print()
        print('Length:',count)
        
    def AddNum123(self,num):
        node = Node(num)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
        
    def AddNum321(self, num):
        node = Node(num)
        current = self.head 
        if self.head == None:
            self.head = node 
        else:
            node.next = current
            self.head = node
   
    def addInBw (self, new, prev):
        new_node = Node(new)
        if self.head == None:
            self.head = new_node    
        else:
            current = self.head
            while current != None:
                if current.data != prev: 
                    current = current.next
                else:
                    new_node.next = current.next
                    current.next = new_node
                    current = current.next
            
    def delNumber(self,num):
        current = self.head
        if current != None and current.data == num:
           self.head = self.head.next       
        else:
            previous = None
            current = self.head
            while current != None and current.data != num:
                previous = current
                current = current.next
            if current != None:
                previous.next = current.next
                
    def nthFromLast(self, n): #by list length
        current = self.head
        length = 0
        while current != None:
            current = current.next
            length += 1
            
        if n > length or n < 1:
            print('lakh di lanet')
        else:
           temp = self.head
           for i in range(length - n):
               temp = temp.next
           print(temp.data)
           
    def kthFromLast(self, k): #by two pointers
        current = self.head
        length = 0
        while current != None:
            current = current.next
            length += 1
            
        if k > length or k < 1:
            print('lakh di lanet')
        else:
            temp = self.head
            pine = self.head
            for i in range(k):
                pine = pine.next
            while pine != None:
                temp = temp.next
                pine = pine.next
            print(temp.data)
    
    def replaceNum(self, a, b): # replace 'a' with 'b'
        current = self.head
    
        if current == None:
            return
        while current != None:
            if current.data == a:
                current.data = b
            current = current.next
            
    def repNumber(self, n, a): #replace node at 'n' with 'a'
        current = self.head
        length = 0
        while current != None:
            current = current.next
            length += 1
            
        if n > length or n < 1:
            return
        else:
            current = self.head
            for i in range(n-1):
                current = current.next
                if current == None:
                    return
            current.data = a
            return
    
    def repNumberr(self, n, a):
        current = self.head
        for i in range(n-1):
            if current != None:
                current = current.next
                if current == None:
                    print('ja pai kam kar')
            current.data = a
            return
        
                
x = LinkList()
x.AddNum123(1)
#x.AddNum123(2)
#x.AddNum123(3)
#x.AddNum123(4)
#x.AddNum123(5)
#x.AddNum123(6)

x.printList()

print('~~~')
x.repNumber(2,' ')
x.printList()

y = LinkList()
y.AddNum321('A')
y.AddNum321('B')
y.AddNum321('C')
y.AddNum321('D')
y.AddNum321('F')
y.AddNum321('G')

print('~~~')
#y.revList()
#y.kthFromLast(3)

'''
n5 = Node('A')
n5.next = Node('B')
n5.next.next = Node('C')

def reversePrint(head):
    if head is None:
        return
    reversePrint(head.next)
    print(head.data)


reversePrint(y.head)
'''
#y.printList()
#print('~~~')

#y.revList()
#y.printList()

#print('~~~')

#x.revList()
#x.printList()
     
       