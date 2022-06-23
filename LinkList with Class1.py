from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()

# $$ print linkedList
# $$ get linkedlist length
# ## print linkedList in reverse-order. (recursion). 
# $$ reverse a linkedList, in-memory (1 <-- 2 <-- 3) ; 3 --> 2 --> 1
# $$ Add/remove
# return 4th last node value. (Two pointer approach)
#  x ---4 -- y
# Kth.
# Update


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class LinkList:
    
    def __init__(self):
        self.head = None #what does self.head do?

    def printList(self):
        current = self.head #how this works here?
        while current != None:
            print(current.data)
            current = current.next
    
    ### int, float, boolean, char, double, long, short ===> STORED ON PROGRAM/FUNCTION STACK
    ### x = 0 --> x=1
    ### OBJECTS (not primitve) ===> HEAP (a separate memory on which objects are stored)

        x = 1; # x = 1. ===> fixed size. int= 4 bytes, COPY-BY-VALUE.
      @0x0  ########
      @0x1  ########
      @0x2  [1]####
      @0x3  ########
      @0x4  [1]#####
        
      ## (int), (float), (bool), str
        y = x  # x = 1, y = 1 --> x-memory-location, y-memory-location.
        y = 3  # x = 1, y = 3 -->
        
        x = obj1 ## x is pointing to memory location of obj1
        y = x    ## copy-by-reference of the memory location.
                 ## y is pointing to the same memory location as of x
                 
      @0x0  ########
      @0x1  ########
      @0x2  node1(5)####
      @0x3  ########
      @0x4  node2########
           ########
      x = node1 ===> x = @0x2
      y = x ====> y = @0x2
          # ==> y.data ==> @0x2.data = 5
          # ---> x.data --> @0x2.data --> latest value = 5
      y = node2 ---> y = @0x4
        
      current = head # current --> 0x2, head --> 0x2
      current = node # current --> 0x4, head --->0x2
        
        
    def AddNum123(self,num):
        node = Node(num)
        if self.head == None:
            self.head = node
            return #without return, infinite loop
        
        current = self.head #how this works here?
        ## currrent ----> Node1 ---> Node2 --> Node3
        ## head ---------- ^
        while current.next != None:
            current = current.next
        current.next = node
        
    def AddNum321(self,num):
        node = Node(num); @0x4
        current = self.head #does not work?
            #   head ---> @0x2
            #   current === ^
        if current == None:
            current = node ## current --> node, head --> None
            ## head = node
            return
        else:
            node.next = current
            #                @0x2  <----- [@0x4] <----- head
            #    current === ^
            
            self.head = node  ## current = node, self.henode

            #                X <--- node <----- current
            #   head    ==== ^
    
    ## 1 --> 2 --> 4; num=3, prev=2
    
    def printValue():
        x = input()
        print("Hello") 
        print("World")
        if x == 2:
            print(x) # 2
            return   # --> wapis
            print("ABCCCC")
        print("anything else")

    
    def addInBw (self,num,prev):
        new_node = Node(num)
        if self.head == None:
            self.head = new_node
            
        else:
            current = self.head
            while current != None: #why current has to be none?
                if current.data != prev: 
                    current = current.next
                else:
                    new_node.next = current.next
                    current.next = new_node
                    current = current.next
            
    ##          10 --> 20 --> 30 --> None
    ## head, current
    ## num=10    
    ###         20  20 --> 30 --> None
                 |_________|      
    def delNumber(self,num):
        current = self.head
        if current != None and current.data == num:
           self.head = self.head.next
            
           
            
           
            current.data = current.next.data #why .data?
            current.next = current.next.next
            
        else:
            previous = None
            current = self.head
            while current != None and current.data != num:
                previous = current
                current = current.next
            if current != None:
                previous.next = current.next
                
                

x = LinkList()
n1 = x.AddNum123(10)
n1 = x.AddNum123(20)
n1 = x.AddNum123(30)
n1 = x.AddNum123(40)

x.printList()
'''
print('~~~')

y = LinkList()
n1 = y.AddNum321(10)
n1 = y.AddNum321(20)
n1 = y.AddNum321(30)
n1 = y.AddNum321(40)

y.printList()

print('~~~')

x.delNumber(20)
y.delNumber(20)
  
x.printList()
print('~~~') 
y.printList()

x.addInBw(35,30)
y.addInBw(45,40)

print('~~~')  

x.printList()
print('~~~') 
y.printList()          
'''        