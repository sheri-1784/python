from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()

def add4Numbers(a,b,c,d):
    sum1 = add(a, b)
    sum2 = add(c, d)
    return sum1 + sum2

def add(a, b):
    sum = a / b
    return sum 

x = add4Numbers(1,2,3,4)
print(x)


list1 = [1, 2, 3, 4] ===> N=4 =====> N = 4-1 = 3

sum1 = 0
for x in range(list1):
    sum1 += list1.get(x)


list1 = [] ==> N = 0, sum1 = 0
list1 = [1] ==> n = 1, sum1 = 1
list2 = [1, 2] ==> n = 2, sum1 = 1 + 2 = 3

list1 = [1, 2, 3, 4]

sum(1,2,3,4)
1 + sum(2,3,4)
1 + 2 + sum(3, 4)
1 + 2 + 3 + sum(4)
1 + 2 + 3 + 4+ sum([]) 

sum(1,2,3,4) ==> 1244
1 + 1243
1 + 2 + 1241
1 + 2 + 3 + 1238
1 + 2 + 3 + 4+ 1234

sum_recursive([1, 2, 3, 4]) /
sum_recursive([2, 3, 4]) / 
sum_recursive([3, 4]) /
sum_recursive([4]) / #3 + sum_recursive([4])
sum_recursive([]) / #sum1 = 4, []


def sum_recursive(list1): # [2, 3, 4]
    if len(list1) == 0:
        return 1234;
    sum1 = getFirstValueOfList(list1); //4
    sumOfRemainingElments = sum_recursive(list1) // [] == > 0
    result = sum1 + sumOfRemainingElments (4 + 0 = 4)
    return result

x = 2344
    x = 5667
