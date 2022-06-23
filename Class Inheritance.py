from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()

'IS A' 
#Employee is a Person
#Dog is an animal'
#Car is a vehicle'

'HAS A'
#library consists of books (both parent and child are independent)

'CONSISTS OF'
#book has 200 pages (page does not exist w/o the book)

class Vehicle:
    def __init__(self,tire,gear,color):
        self.tire = tire
        self.gear = gear
        self.color = color
        
    def show(self):
        print('A Vehicle has',self.tire,'tires')
        print('A Vehicle has',self.gear,'gears')
        print('A Vehicle has',self.color,'color')
        
class Car(Vehicle):
    def __init__(self,v, typo,drive,seat):
        super(v.tire, v.gear, v.color)
        self.typo = typo
        self.drive = drive
        self.seat = seat
        
    def show(self):
        
        super().show()
        #show()
        print('A CAR has',self.tire,'tires')
        print('A CAR has',self.gear,'gears')
        print('A CAR has',self.color,'color')
        
    def add(a, b):
        return a+b
    def add (a, b, c):
        return a + b +c
    

'''        
class Brand(Car):
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def br_show(self):
        print('A vehicle has',self.tire,self.gear,self.color)
        print('A car can be',self.typo,self.drive,self.seat,'seater')
        print('My car is',self.brand,self.model,self.year)
'''        
vehicle = Vehicle(4,'Auto','blue')
#vehicle.show()
tycar1 = Car(vehicle,'SUV','4x4',7)

tycar1.show()

Vehicle v = new Vehicle()
v.show() ---> 1 meter.

Car c = new Car()
c.show() --> 15 meter.

print(c.add(2, 3))
print(c.add(2, 3 , 4))




Bus b = new Bus()
bus.show() --> length =41 meter

Vehicle v1 = new Car()
v.show() -->
Vehicle v2 = new Bus()
v2.show() --> 41 meter.

vehicles = [v1, v2]

for x in range(2):
    if issubclassof(vehicles[x], Car):
        print ("Do this")
    else:
        print("Do that")
    vehicles[x].draw()

Map parent
    HashMap<> --- key --> value pair.
    SortedHashMap -----> keys are sorted in ascending order.
    TreeMap --> data is stored in tree structure.

process_map(HashMap map){
    
    print(all elements in the map)
}

process_map(SortedHashMap map){
    
    print(all elements in the map)
}

process_map(TreeMap map){
    
    print(all elements in the map)
}

process_map(Map map){}

add_two_numbers(a,b)
add_tthree_(a,b,c)


#tycar = Car('SUV','4x4',7)
#tycar.car_show()
#mycar = Brand('Honda','Pilot',2016)

#mycar.br_show()
        