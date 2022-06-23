from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()


List vs Stack (LIFO) vs Queue (FIFO)

list = [1, 2, 3]

list.append(4) --> [1, 2, 3, 4]
list.remove(index=1) --> [ 1, 3, 4]
list.pop() ---> [1, 2, 3]


push vs pop.

|  4   | 
|  3   |
|  2   |
|__1___|

stack = Stack.new
stack.push(4)
stack.pop() --> returns 4.
stack.size()/ length() --> stack size.


Stack could be implemented with List or LinkedList.
[1, 2, 3, 4]     ---> Array implementation
1 --> 2 --> 3 --> 4 --> LinkedList implementation


Queue --> First-in, First-out.

q = Queue.new 
q.offer(1) --> Add. [1]
q.poll() --> pop First element.

class Queue{
    queue = []       
    Queue(){}
    
    def offer()
    def poll();        
        
}

q = Queue.new
q.offer()
q.poll()




Binary-Tree - Level Order Traversal.

    1
    
  2    3

queue.add(root=1); queue = [1]

# Python program to demonstrate
# stack implementation using a linked list.
# node class

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class Stack:

	# Initializing a stack.
	# Use a dummy node, which is
	# easier for handling edge cases.
	def __init__(self):
		self.head = Node("HEAD")
        
		self.size = 0

        self.q = []

	# Push a value into the stack.
	def push(self, value):
		node = Node(value)
		node.next = self.head.next
		self.head.next = node
		self.size += 1
        
    def lpush(self, x):
        self.q.append(x)
        
    def pop(self):
        if empty():
            return
        num = self.q.pop()
        return num
        

	# Remove a value from the stack and return.
	def pop(self):
		if self.isEmpty():
			raise Exception("Popping from an empty stack")
		remove = self.head.next
		self.head.next = self.head.next.next
		self.size -= 1
		return remove.value



HEAD.next = None
head.next = 2
2.next = None

head -->3-->2 --> None
head -->2 --> None

node = Node(3)
3.next = 2
head.next = 3

rem = 3
head.next = 3.next
return 3


# Driver Code
if __name__ == "__main__":
	stack = Stack()
    stack.push("2")
    stack.push("3")
    stack.pop()

|
|   4
|   3
|___2_



HEAD --> None
HEAD --> 2 -- None
HEAD --> 2 -- 3 --> None
HEAD --> 2 -- 3 --> 4 --> None

HEAD --> 2 -- 3 --> None (pops 4)
HEAD --> 2 -- None (pop 3)


HEAD
HEAD --> 2
HEAD --> 3 --> 2
HEAD --> 4 --> 3 --> 2

HEAD.next = 4.next
HEAD --> 3 --> 2


[]
[2]
[2, 3]
[2, 3, 4]
[2, 3] => pop = 4
[2] => pop = 3
[] => pop 2


[]
[2]
[2, 3]
[2, 3, 4]
[3, 4] pop(0) = 2
[4] pop(0) = 3
[] pop(0) = 4

head
head --> 2 --> None
head --> 2 --> 3 --> None
head --> 2 --> 3 --> 4 --> None

node.next= tail.next
tail.next = node
tail = tail.next (5)
  
    




