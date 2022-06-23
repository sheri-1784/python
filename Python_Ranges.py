from time import sleep

def cls():
    print("\033[2J\033[;H", end='')
    sleep(0.1)

cls()
'''
for value in range(0,5):
    print((value**2)/(2**3))

number = list(range(0,11)) #creates a list for number 1-10
print(number)

number1 = [1,2,3,4,555,6] #creates list of random numbers
print(number1)

cars = ['bmw', 'honda', 'audi', 'gmc']
for car in cars:
    if (car=='bmw') or (car=='gmc'):
        print(car.upper())
    else:
        print(car.title())
        
car1 = 'tesla'
if car1 not in cars:
    print(car1.title())

for car in cars:
    if car == 'bmw':
        print('\nSorry,', car.upper(), 'not washed')
    else:
        print('\tWashing your',car.upper())
print('\nFinished wahing all cars.')

bikes = []
#bikes.append('Honda')
if bikes:
    for bike in bikes:
        print('Your',bike,'is washed\n')
else:
    print('\nYou sure, you dropped your bike?\n')

cars = ['tesla','lucid','honda','bmw','gmc']
e_cars = ['tesla','lucid','rivian']
for car in e_cars:
    if car in cars:
        print(car.title(),'is a good EV')
    else:
        print(car.title(),'is also a good EV')        
'''
age = int(input('Please enter your age: '))
child = 'Free'
teen = 10
adult = 25
senior = 15

if age <= 5:
    print('Your ticket is',child)
elif age > 5 and age <= 18:
    print('Your ticket is USD',teen)
elif age > 18 and age <= 60:
    print('Your ticket is USD',adult)
else:
    print('Your ticket is USD',senior)

