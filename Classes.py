from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()
'''
class Dog:
    species = 'Pet'
    def __init__(self,x,y): #constructor method
        
        self.name = x
        self.age = y
buddy = Dog('buddy',4)
print(f'{buddy.species} is not a pet breed')
print(f'{buddy.name} is a very zaleel kutta')
print(f'{buddy.age} is not that zaleel')

print('---------------------')
kuddy = Dog('kuddy',6)

print(f'{kuddy.species} is not a pet breed')
print(f'{kuddy.name} is a very zaleel kutta')
print(f'{kuddy.age} is not that zaleel')

print('---------------------')
muddy = Dog('muddy',9)

print(f'{muddy.species} is not a pet breed')
print(f'{muddy.name} is a very zaleel kutta')
print(f'{muddy.age} is not that zaleel')
'''
class Dog:
    species = "Canis familiaris"

    def __init__(self, x, y):
        self.name = x
        self.age = y

    # Instance method
    def show(self):
        desc = f"{self.name} is {self.age} years old"
        return desc

    # Another instance method
    def speak(self,sound):
        return f"{self.name} speaks {sound}"
    
    # and yet another instance method
    def breed(self):
        mads = f'{self.name.title()} is a half-wolf'
        return mads

buddy = Dog('budd',7)
print(buddy.show())
print(buddy.speak('French'))
print(buddy.breed())
print('--------------------')
todd = Dog('Todd',5)
print(todd.show())
print(todd.speak('English'))
print(todd.breed())
'''
class employee:
    company = 'Sadara'
    def __init__(self,name,pay,city):
        self.name = name
        self.__pay = pay
        self.city = city
        
    def change_pay(self,new_pay):
        self.__pay = new_pay

    def show(self,city):
        self.city = city
        bio = f"""
  Employee Name = {self.name}
  Company Name = {self.company}
  Employee Pay = {self.__pay}
  Employee City = {self.city}"""
        return bio

emp1 = employee('Kamil',12000,'Khobar')
#emp2 = employee('Haris',10000, 'Damam')

emp1.change_pay(500)
print(emp1.show('NYC'))
#print(emp1.__pay)

pi = 3.14
class Circle:
    pi = 3.14
    def __init__(self,radious):
        self.radious = radious
        
    def calc_area(self):
        print('Are of Circle is: ',pi*self.radious**2)
        
class Cylinder:
    pi = 3.14
    def __init__(self,radious,height):
        self.radious = radious
        self.height = height
    
    def calc_area(self):
        print('Are of Cylinder is: ',pi*self.radious**2*self.height)
        
def area(shape):
    shape.calc_area()
    
cir = Circle(5)
cyl = Cylinder(5,5)

area(cir)
area(cyl)

class Vehicle:
    def __init__(self, name,color,price):
        self.name = name
        self.color = color
        self.price = price
        
    def info(self):
        print(self.name, self.color, self.price)
        
class Car(Vehicle):
    
    def gear(self,num):
        print(self.name,'has',num,'number of gears')
        
mycar = Car('Audi','Blue',35000)

mycar.info()
mycar.gear(5)
print('--------------------')

class Vehicle:
    def __init__(self, name,color,price):
        self.name = name
        self.color = color
        self.price = price
        
    def info(self):
        print(self.name, self.color, self.price)
        
class Car(Vehicle):
    
    def __init__(self,gear):
        self.gear = gear
    
    def box(self):
        print(self.name,'has',self.gear,'number of gears')
        
mycar = Car('Audi','Blue',35000,5)

mycar.info()
mycar.box()

class Person:
    
    def __init__(self,name, age, sex, prof):
        self.name = name
        self.age = age
        self.sex = sex
        self.prof = prof
        
    def bio(self):
        print('Name:',self.name,'\nAge:',self.age,'\nSex:',self.sex)
        
    def work(self):
        print(self.name,'works as',self.prof)
        
hum1 = Person('Jessy',35,'Male','Engineer')
hum2 = Person('Maya',33,'Female','Lawyer')

hum1.bio()
hum1.work()
print()
hum2.bio()
hum2.work()

class Student:
    school = 'Millat'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def info(self):
        print(self.name,'is aged',self.age,'and goes to',Student.school)
        
    def x_age(self,new_age):
        self.age = new_age
        
    @classmethod
    def schoolx(cls,new_name):
        Student.school = new_name
    pass
    
x1 = Student('Mike',14)
x1.info()

x1.name = 'Majed'
x1.x_age(18)
Student.schoolx("Islamia")
x1.info()

print(x1.name)
del x1.name

print(x1.name)

class Person:
    
    def __init__(self): #Non-Parametrized Constructor
        self.name = 'Jessy'
        self.age = 35
        self.sex = 'male'
        self.prof = 'Actor'
        
    def bio(self):
        print('Name:',self.name,'\nAge:',self.age,'\nSex:',self.sex)
        
    def work(self):
        print(self.name,'works as',self.prof)
        
hum1 = Person()


hum1.bio()
hum1.work()

class Person:
    city = 'NYC'
    def __init__(self,name, age, sex, prof):
        self.name = name
        self.age = age
        self.sex = sex
        self.prof = prof
        
    def bio(self):
        print('Name:',self.name,'\nAge:',self.age, #break
              '\nSex:',self.sex,'\nCity:',Person.city)
        
    def work(self):
        print(self.name,'works as',self.prof)
        
hum1 = Person('Mansha',32,'Female','Actor')
hum2 = Person('Ashar',12,'male','writer')


hum1.bio()
hum1.work()
print('------------')
hum2.bio()
hum2.work()
print('------------')

print('Name:',getattr(hum1,'name'))
print('Name:',getattr(hum2,'name'))

print('Age:',getattr(hum1,'age'))
print('Age:',getattr(hum2,'age'))

hum1.pay = 10000
hum2.pay = 12000
print('------------')
print(hum1.pay)
print(hum2.pay)

#del hum1.pay
#delattr(hum2,'pay')

#print(hum1.pay)
#print(hum2.pay)
print('------------')
hum1.bio()
hum1.work()

print('------------')
print(hum1.__dict__)
for key in hum1.__dict__.items():
    print(key[0].title(),':',key[1])

class Student:
    school = 'Millat'
    def __init__(self, name, roll, age):
        self.name = name #cannot be accessed outside Class
        self.roll = roll
        self.age = age
        
    def show(self):
        print(self.name, self.roll,self.age)
        
    def update(self,roll,age):
        self.roll = roll
        self.age = age
        
    def ad_marks(self,marks):
        self.marks = marks
        #print(self.school)
        #print(Student.school)
        
emma = Student('Emma',88,10)
emma.show()

emma.update(76,12)
emma.show()

emma.ad_marks(99)
print(emma.name,'scored',emma.marks,'marks')

emma.marks = 77
print(emma.name,'scored',emma.marks,'marks')

#print(self.school) self does not work outside the class
print(Student.school) #to access an att outside a class
print(emma.school) #to access an att outside a class

Student.school = 'Islamia'
print(Student.school)
print(emma.school)

emma.school = 'Johar'
print(Student.school) #why its giving value from prev name because when
#we use the object name to change the class var, it only changes for
#that particualr object. Use class name for a permanent change.
print(emma.school)

Student.school = 'Government'
print(Student.school)
print(emma.school)

emma.school = 'John'
print(Student.school)
print(emma.school)


class Language:
    course = 'Python'
    
class Student(Language):
    course = 'Ruby'
    
    def __init__(self,name):
        self.name = name
        
    def show(self):
        print(self.name,'is learning',Student.course)
        
        Language.course = 'Golang'
        print(self.name,'is learning',Language.course)
        
emma = Student('Emma')
emma.show()

# Student.course changes var at child class level
# Language.course changes var at parent class level
# self is not accessible outside the class
# Class.Var is accessible outside the class

class Student:
    school = 'Westwind'
    
    def __init__(self,name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def show(self):
        print('Name:',self.name,'Age:',self.age)
        
    def bio(self, course):
        print(self.name,'is a grade',self.grade,'student')
        print('and studies', course,'at',Student.school)
        
    def new_age(self,xage,xgrade):
        self.age = xage
        self.grade = xgrade
        
    @classmethod
    def new_school(cls,new_schl):
        cls.school = new_schl 
    
s1 = Student('Samar',10,4)
s1.show()
s1.bio('English')
print()
s1.new_age(14,6)
s1.new_school('Fernbank')

s1.show()
s1.bio('Maths')  

class Employee:
    
    def show(self,name,company):
        print(name,'works for',company)
        
emp = Employee()
emp.show('Shahryar','Accenture')

class Employee:
    
    def __init__(self):
        self.name = 'Shahryar'
        self.comp = 'Sadara'
    
    def show(self):
        print(self.name,'worked for',self.comp)
        
emp = Employee()
emp.show()

class Employee:
    company = 'Accenture'
    
    def __init__(self,name,pay,dept = 'Sourcing',loca = 'Toronto'):
        self.name = name
        self.pay = pay
        self.dept = dept
        self.loca = loca
        
    def show(self):
        print(self.name,'works in',self.dept,'at',Employee.company)
        print('He makes CAD',self.pay,'and lives in',self.loca)
        
emp1 = Employee('David',105000)
emp1.show()

emp2 = Employee('Marc',150000,'Legal','Chicago')
emp2.show()

class Company:
    comp = 'Accenture'
    count = 0
    
    def __init__(self,bizz):
        self._bizz = bizz #protected variable
        Company.count += 1 #constructor call count
        
class Depart(Company):
    
    def __init__(self,bizz,dname):
        super().__init__(bizz) #copy parent constructor
        self.dname = dname
        
class Employee(Depart):
    
    def __init__(self,bizz,dname,name,eid,pay):
        super().__init__(bizz,dname) #copy parent constructor
        self.name = name
        self.eid = eid
        self.__pay = pay #provate variable
        
    def show(self,city):
        print(self.name,'works for',Company.comp)
        print(Company.comp,'is known for',self._bizz)
        print('But',self.name,'works in',self.dname)
        print('His enterprise ID is',self.eid)
        print('Currently he is located in',city)
        print('Currently he is paid CAD',self.__pay)
    
        
emp1 = Employee('IT','Sourcing','Matt',1002607,100000)
emp1.show('Ottawa')
print(Company.count)

emp2 = Employee('IT','Sourcing','Jay',1002608,110000)
emp2.show('Ottawa')
print(Company.count)

emp3 = Employee('IT','Sourcing','Amit',1002609,120000)
emp3.show('Ottawa')
print(Company.count)

emp1.name = 'David' #update object name
emp1.show('Toronto')
print(Company.count)

emp1._Employee__pay = 150000
print(emp1.name,'gets paid CAD',emp1._Employee__pay)
#access private attribute

class Student:
    
    def __init__(self,name,age):
        self.name = name
        self.__age = age
        
    def get_age(self): #enables pvt var access outside
        return self.__age
        
    def set_age(self,agex): #enables change to pvt var outside.
        self.__age = agex
        
std = Student('Emma',12)
print('Name:',std.name,'Age:',std.get_age())

std.set_age(14)
print('Name:',std.name,'Age:',std.get_age())

#POLYMOSPHISM:

class Vehicle:
    
    def __init__(self,name, price):
        self.name = name
        self.price = price
        
    def show(self):
        print('Name:',self.name,'Price:',self.price)
        
    def speed(self):
        print(self.name,'has max speed of 100km/hr')
        
    def make(self,made):
        print(self.name,'is made in',made)
        
class Car(Vehicle):
    
    def __init__(self,name,price,brand):
        super().__init__(name,price)
        self.brand = brand
        
    def show(self):
        print('Name:',self.name,'Price:',self.price)
        print(self.brand,'makes an excellent',self.name)
    
    def speed(self,speed):
        print(self.name,'has max speed of',speed)
        
    def make(self,made):
        print(self.name,'is made in',made)
        
        
truck = Vehicle('Truck','$25,000')
truck.show()
truck.speed()
truck.make('China') 

print()

car = Car('CX9','$45,000','Mazda')
car.show() 
car.speed('240km/hr')
car.make('Japan')

class Shopp:
    
    def __init__(self,basket,name):
        self.basket = list(basket)
        self.name = name
        
    def show(self):
        for item in self.basket:
            print(self.name,'purchased',item)
        
    def __len__(self):
        count = len(self.basket)
        return count * 2
    
grocer = Shopp(['rice','oil','cake'],'Maha')
grocer.show()
print(len(grocer)) 

class Honda:
    
    def __init__(self,model, price):
        self.model = model
        self.price = price
        
    def show(self,speed):
        print(self.model,'runs at',speed)
        print(self.model,'is priced at at',self.price)

class Mazda:
    
    def __init__(self,model, price):
        self.model = model
        self.price = price
        
    def show(self,speed,city):
        print(self.model,'runs at',speed)
        print(self.model,'is priced at at',self.price)
        print(self.model,'is made in',city)
        
honda = Honda('Accord','$25,000')
mazda1 = Mazda('CX-90','$35,000')
mazda2 = Mazda('CX-50','$15,000')

def dash(car): #polymorphism with function.
    if car == honda:
        car.show('250km/hr')
    else:
        car.show('220km/hr','Nepean')
    print()
    
dash(honda)
dash(mazda1)
dash(mazda2)
    

for car in [honda, mazda1, mazda2]:
    if car == honda:
        car.show('200km/hr')
    else:
        car.show('180km/hr','Nepean')
    print()