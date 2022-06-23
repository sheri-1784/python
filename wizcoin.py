from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()

class WizCoin:
    def __init__(self,g,s,k):
        self.g = g
        self.s = s
        self.k = k
        
    def value(self):
        return (self.g*29*17 + self.s*29 + self.k)
    
    def weight(self):
        return(self.g*31.103 + self.s*11.34 + self.s*5.0)