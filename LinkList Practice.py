from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

head = Node(12)

node2 = Node(14)
head.next = node2

node3 = Node(16)
node2.next = node3

node4 = Node(20)
node3.next = node4

def PrintList(head):
    current = head
    while current != None:
        print(current.data)
        current = current.next

PrintList(head)

def addNumber(head, num1,num2):
    new_node = Node(num1)
    if head == None:
        return new_node #try making a change
    while head != None:
        if head.data != num2:
            head = head.next
        else:
            new_node.next = head.next
            head.next = new_node
            head = head.next
             

addNumber(head,18,20)          
print('---')
PrintList(head)
'''
def deleteNumber(head, num):
    if head.next.data != num:
        head = head.next
        head.next = head.next.next
        
deleteNumber(head,18)
print('---')
PrintList(head)
'''

def delNumber(head, num):
    if head != None and head.data == num:
        head.data = head.next.data
        head.next = head.next.next
    else:
        previous = None
        current = head
        while current != None and current.data != num:
            previous = current
            current = current.next
        if current != None:
            previous.next = current.next

delNumber(head,12)
print('---')
PrintList(head)
#print('*******')

'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
  
def printList(head):
    current = head
    while current != None:
        print(current.data)
        current = current.next       

def printList(head):
    current = head
    while current != None:
        print(current.data)
        current = current.next
    return
  
def addNumber(head,num1, num2):
    new_item = Node(num1)
    if head == None:
        return new_item
    current = head
    while current != None:
        if current.data != num2:
            current = current.next
        else:
            new_item.next = current.next
            current.next = new_item
            current = current.next
    return

def addNumber(head, num1,num2):
    new_node = Node(num1)
    if head == None:
        return new_node
    current = head
    while current != None:
        if current.data != num2:
            current = current.next
        else:
            new_node.next = current.next
            current.next = new_node
            current = current.next
           
def delNumber(head,num):
    current = head
    if current == None:
        return
    while current != None:
        if current.data != num:
            current = current.next
        else:
            current.next = current.next.next
   
def delNumber(head,num):
    previous = None
    current = head
    while current != None and current.data != num:
        previous = current
        current = current.next
    if current != None:
        previous.next = current.next
           
       

head = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

head.next = node2
node2.next = node3
node3.next = node4

printList(head)

addNumber(head,24,20)
print('---')
printList(head)

delNumber(head,24)
print('---')
printList(head)
'''

    
            
        
    
    
    