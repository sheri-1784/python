from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()


def powOftwo(x):
    n = 10
    for i in range(n):
        y = 2**i # y = 2^0 = 1
        print("Inside the loop with i=" + str(i) + "\n\n")
        if x == y: 
            return True
        else:
            return False
    print("Out of for loop")

print(powOftwo(2))

'''
N = 16
N = 17

N == 2 ^ x

x = 0
while (2 ^ x <= N): # 2^5 = 32 <= 17
    x = x + 1 # x = 5
if 2^(x-1) == N:
    return True
return False

2 ^ x <= N

recurse(N, 0)

def recurse(N, x):
    if 2 ^ x == N:
        return True
    if 2 ^ x > N:
        return False
    output = recurse(N, x+1)
    return output
'''







