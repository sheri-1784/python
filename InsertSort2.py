from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()

x = [3,1,7,5,4]
def inSort(x):
    for j in range(1,len(x)):
        k = x[j]
        i = j-1

        while i >= 0 and x[i] > k:
            x[i+1] = x[i]
            i = i-1
        x[i+1] = k
    return x

m = inSort(x)
print(m)