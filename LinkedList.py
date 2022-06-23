from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        #return
   

#Node ==> (data, next)

head = Node(1)
#head.data = 1 #next --> None

node2 = Node(15)
#node2.data = 15 #next --> None

head.next = node2
    # head --> node2 --> None
    
node3 = Node(3)
node2.next = node3



# head --> node2 --> node3 --> None

# ---------------------- print all elements of linkedlist


# node1 --> node2 --> node3 --> None
#                               head

def printList(head):
    #start = head, end = None
    while(head != None):
        print(head.data)
        head = head.next
    

printList(head)

# ------------------ Add a number=12 between 15 and 3 ----

#BEFORE
#1 ==> 15 ==> 3
# After
#1 ==> 15 ==> 12 ==> 3

#step#1
#node4 = Node(12)

# step#2
# (15 ==> 3) --> not clear
# 12 ==> 3

# step#3
# 15 ==> 12 (==> 3)

def addNumberToList(abc, number):
    node = Node(number)
    if abc == None:
        return node
    while(abc != None):
        if abc.data != 15:
            abc = abc.next
        else:
            node.next = abc.next #step2 
            abc.next = node #step3
            abc = abc.next

#1 ==> 15 ==> 12 ==> 3
#             abc
addNumberToList(head, 12)
print("---")
printList(head)

# ------------- delete number 15 from the list

# abc = 1 (abc is pointing to 1)
## 1 ==> 15 ==> 12 ==> 3 
## 1 =========> 12 ===> 3

def removeNumberFromList(abc, number):
    while(abc.next.data != 15):
        abc = abc.next
    abc.next = abc.next.next

## 1 ==> 15 ==> 12 ==> 3 ==> 11 ===> 9 ==> 10 --> None
## 1 ==> 15 ==> 12 ========> 11 ===> 9 ==> 10
'''     
current = 1
previous = None

previous = current
current = 15

previous = current = 15
current = 12
 
previous = current = 12
current = 3

previous.next = current.next
'''

def removeNumberFromList(head, number):
    previous = None
    current= head
    while(current != None and current.data != number):
        previous = current
        current = current.next
    if current != None:
        previous.next = current.next

removeNumberFromList(head, 15)
print("---")
printList(head)
        