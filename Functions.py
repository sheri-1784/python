from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()

'''
def greet_user(user):
    print('Hello,',user.title())
greet_user('shahryar')

def find_pet(name,pet='dog'):
    print('My',pet,'is very loving pet')
    print('His name is',name.title())

'''  
def print_stars():
    x = 1
    y = int(input('Stars: '))+1

    while x < y:
        n = 0
        while n < y-x-1:
            print(' ', end = ' ')
            n = n+1
        m = 0
        while m < x:
            print('*',end = ' ')
            m = m+1
        print()
        x = x+1

    a = 1
    b = y-1

    while a < b:
        m = 0
        while m < a:
            print(' ', end = ' ')
            m = m+1
        n = 0
        while n < b-a:
            print('*',end = ' ')
            n = n+1
        print()
        a = a+1

x = 0
while x < 5:
    print_stars()
    x = x+1
'''
find_pet('harry')

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('kutta','harry')

def name(first,last,middle=''):
    if middle:
        full_name = f'{first} {middle} {last}'
    else:
        full_name = f'{first} {last}'
    return full_name.title()
musician = name('harry','porter','perry')
print(musician)

def person(firstn,lastn,middle='',age=None):
   full_name = {'first':firstn,'last':lastn}
   if middle:
       full_name['mid'] = middle
   if age:
       full_name['age'] = age
   return full_name
musician = person('harry','porter','kaka',27)
print(musician)
print(musician['first'].title())
musician['first'] = 'Perry'
print(musician)

def name(first,last,middle=''):
    if middle:
        full_name = f'{first} {middle} {last}'
    else:
        full_name = f'{first} {last}'
    return full_name.title()

while True:
    print('First and last name: ')
    f_name = input('First Name: ')
    if f_name == 'q':
        break
    l_name = input('Last Name: ')    
    if l_name == 'q':
        break
musician = name(f_name,l_name)
if f_name == 'q' or l_name == 'q':
    print('No name was entered')
else:
    print('My full name is:',musician)

def greet(names):
    for name in names:
        message = f'Hello, {name.title()}!'
        print(message)
names = []
names.append(input('Name: '))
names.append(input('Name: '))
names.append(input('Name: '))
names.append(input('Name: '))
greet(names)
print(names)

ups = ['phone','robot','bike']
pns = []

for i in range(len(ups)):
    pns.append(ups[i])
for pin in pns:
    print(pin.title())
'''