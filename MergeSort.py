from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()

def mergeSort(x): # x = [5,3,7,8, 1]
    if len(x) > 1: # x 
        m = len(x)//2 # m = 1; 
        
        l = x[:m] # l = [7]
        r = x[m:] # r = [1, 8]
        
        mergeSort(l) # l = [7] ==> return         
        mergeSort(r) # r = [8, 1] ==> return [1, 8]
        
        #mergeLeftAndRight(l, r) #  ===> [1, 7, 8]
        
#def merge(l, r, x):
        i = j = k = 0
        
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                x[k] = l[i]
                i = i+1
            else:
                x[k] = r[j]
                j = j+1
            k = k+1
            
        while i < len(l):
            x[k] = l[i]
            i = i+1
            k = k+1
            
        while j < len(r):
            x[k] = r[j]
            j = j+1
            k = k+1

            
b = [5,3,7,1,8]
mergeSort(b)
print(b)
        