from time import sleep

def cls():
    print("\033[2J\033[;H", end='')
    sleep(0.1)

cls()
'''
bikes = [] #starts an empty list
bikes.append('honda') #appends items at the end of the list
bikes.append('yamah')
bikes.append('panda')
bikes.insert(0,'kaka') #adds items at index 0
bikes[1]='bmw' #adds item at index 1

for bike in bikes:
    print('I have a',bike.upper(),'bike.')
    print('I hate',bike,'\n')
   
for bike in bikes:
    print('I love',bike)
   
square = [] #creates an empty list
#creating a list of numbers with range and loop
for val in range(1,12): #use a range function with loop
    sq = val**2 #create a variable for list
    square.append(sq) #append the variable to list
print(square)

square = [] #same as above
for val in range(1,11):
    square.append(val**2) #append the variable directly to the list
print(square)

#print(min(square1))
#print(max(square1))
#print(sum(square1))

for value in range(1,22,3):
    print(value) #this does not create a list but returns individual values
'''
sugar = [val**2 for val in range(1,5)]
print(sugar) #list comprehension - compiling the code in a single line.

print([val**3 for val in range(1,5)]) #prints a list but not named

print(sum(sugar))
print(min(sugar))
