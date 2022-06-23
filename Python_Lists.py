from time import sleep
def cls():
    print("\033[2J\033[;H", end='')
    sleep(0.1)
cls()
'''
bike = [] #start with an empty list
bike.append('yamah') #add item at the end
bike.append('ducati')
bike.append('honda')
print(bike)
print(bike[0].upper()) #print items at location 0
print(bike[1].upper())
bike[1] = 'panda' #replaced item at position 1
print(bike)
bike.insert(0,'kaka') #inserts item at index 0
print(bike)
bike.insert(0,'drone') #insert 'drone' at index 0
print(bike[0].upper())
print(bike)
del bike[-1] #deleted last item in the list
print(bike)
p_bike = bike.pop() #pops last items from list. 
#The item is removed from the list but still stays 
#in the code and can be used.
print(p_bike)
print("I used to love",p_bike.upper())
print(bike)
print('The last bike I owened was',bike[-1].title()) 
#this prints the last item in the list.
print(bike)
print('The 2nd bike I owned was',bike.pop(1)) 
#this pops the item at index 1
print(bike)
bike.remove('yamah') #removes the named item from the list.
print(bike)
cars = ['honda', 'bmw','tesla','audi']
cars.sort() #sorts the list in alphabetial order permanently
print(cars)
cars.sort(reverse=True) #sorts the list in reverse order
print(cars)
print(sorted(cars)) #sorts the list temporarily
print(cars)
cars.reverse() #reverse the list order
print(cars)
cars.reverse()
print(cars)
print(len(cars)) #provides the length of a list
cars.insert(0,'toyota') #inserts an item at index 0
print(cars)
print(cars[0].upper())
cars[0] = 'gmc' #replaces item at index 0
print(cars)
print(sorted(cars))
print(cars)
cars.reverse()
print(cars)
print("The length of the list is:",len(cars))
print('I love cars from',cars[-1].upper())

number = [1,2,3,4,5,6,7,8,89,]
print(min(number))
print(max(number))
print(sum(number))

player = []
player.append('kaka')
player.append('mama')
player.append('khan')
player.append('bhai')
#print(player)
print(player[-2:]) #prints the last 4 items in a list
print(player[:2]) #prints from the stated index
#player.reverse()
player.sort(reverse=True)
print(player)

for x in player[:4]:
    print(x.title(),end=' ')

   
sport = player[:] #copy list - this is to create a new list
print(sport)

sport.append('maja')
print(sport)

hockey = sport #this does not create a new list. 
#Both names refer to the same list.
print(hockey)

hockey.append('boota')
sport.append('choocha')

print(hockey)
print(sport)

printer = ('hp','sam','apple') #tuple with strings. 
#values remain fixed. cant be changed.
print(printer)

number = (200,10,1) #tuple with numbers. remains fixed. 
#cant be changed/sorted.
print(number)
for num in number: #for loop can be applied to tuples
    print(num**2)

number = (1,10,200) #for loop on a tulip
for num in number:
    print(num**(2))

for val in range(5):
    print('hello')
    print('\tworld')
'''
bike = []
for value in range(10,0,-1):
    bike.append(value)
print(bike)
    