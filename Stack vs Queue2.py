from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()

class Stack:
    def __init__(self):
        self.q = []
        
    def push(self, x):
        self.q.append(x)
        
    def popp(self):
        if not self.q:
            print('Empty List')
        else:
            num = self.q.pop()
            return num
    
    def size(self):
        return len(self.q)
    
    def prinList(self):
        print(self.q)
        
class Queue:
    def __init__(self):
        self.q = []
        
    def push(self, x):
        self.q.append(x)
        
    def popp(self):
        if not self.q:
            print('Empty List')
        else:
            num = self.q.pop(0)
            return num    

    def prinList(self):
        print(self.q)        
        

mist = Queue()
mist.push(1)
mist.push(2)
mist.push(3)
mist.push(4)
mist.push(5)

mist.prinList()

print(mist.popp())
print(mist.popp())
mist.prinList()


        