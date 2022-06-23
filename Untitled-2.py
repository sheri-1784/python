def mergeSort(x):
    if len(x) > 1:
        m = len(x)//2
       
        l = x[:m]
        r = x[m:]
       
        mergeSort(l)      
        mergeSort(r)
        merge(l,r,x)
       
 
def merge(l,r,x):
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