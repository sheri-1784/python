from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()

from datetime import date

class Student:
    # Constructor
    count = 0
    def __init__(self, A, age):
        self.name = A
        self.age = age
        
    '''
    @classmethod
    def create_student_by_birth_year(cls, X, birth_year):
        return Student("Jessica", date.today().year - birth_year)
#        std = Student(name, age)
#        return std

    @classmethod
    def create_student_by_age(cls, name, age):
        return Student(name, age)
#        std = Student(name, age)
#        return std
    
    @classmethod
    def methodB(cls, age):
        if cls.count == 2:
            print('Only two objects are allowed')
            return None
        cls.count += 1
        std = Student('Jessa', age)
        return std
    '''    
    abc = 4
    def create_student_by_birth_year(birth_year):
        Student.abc = 10
        return Student("Jessica", date.today().year - birth_year)


    def show(self):
        print(self.name + "'s age is: " + str(self.age))
        


jessa = Student.create_student_by_birth_year(1990)
print(Student.abc)
jessa.show()
#print(Student.count)

#jessa = Student.methodB(50)
#jessa.show()
#print(Student.count)

#jessa = Student.methodB(30)
#jessa.show()
#print(Student.count)
# create new object using the factory method
#joy = Student.create_student("Joy", 1995)
#print(joy)

#jessica = Student.create_student('jessica',22)
#print(jessica.name,'is',jessica.birth_year,'old')




