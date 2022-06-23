
def InSort(x):
    for j in range(1,len(x)):
        k = x[j]
        i = j-1       
        while i >= 0 and x[i] > k:
            x[i+1] = x[i]
            i = i-1
        x[i+1] = k
    return x

y = [3,5,4,2,1]
print(InSort(y))

def minSort(x):
    b = []
    while x:        
        for i in range(len(x)):
            if x[i] == min(x):
                q = x.pop(i)
                b.append(q)
                break
    return b
b = [3,4,5,7,2,1,3,4,6]
print(minSort(b))

a = [23,45,24,56,89,54,67]

while a:
    c = min(a)
    for i in range(len(a)):
        if a[i] == c:
            print(a.pop(i),end=' ')
            break

print()

def newSort(a):
    for j in range(1,len(a)):
        x = a[j]
        i = j-1
        while i >= 0 and a[i] < x:
            a[i+1] = a[i]
            i = i-1
        a[i+1] = x
    return a
    
b = [3,4,6,7,9,8,1]
print(newSort(b))