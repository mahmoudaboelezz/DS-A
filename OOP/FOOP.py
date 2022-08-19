""" # maxHealth = 700
# currHp = 100

# def setHP(item):
#     global currHp
#     currHp += item
#     if currHp > maxHealth:
#         currHp = maxHealth
#     print(currHp)

# gem = 1000
# setHP(gem) """

""" class Student:
    #class attributes shared for all the class functions
    no_of_students = 0
    #we can add default values to prevent error from missing required arguement
    def __init__(self,name ,age, courses):
        #instants attrbutes "public attributes"
        self.age = age
        self.courses = courses
        #private attributes
        self.__name = name
        #reference by class attribute
        Student.no_of_students += 1


    #encapsulation
    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    #instants methods
    def describe(self):
        print(f"Name: {self.__name} , Age: {self.age} and Courses: {self.courses}")


    def is_old(self, num):
        if self.age <= num:
            print("Student is Not old")
        else:
            print("Old!")


    

student_1 = Student("Mahmoud" , 23 ,['cs','math1'])
student_1 = Student("Ahmed" , 24 ,['cs','math2'])
# student_1.describe()
# student_1.is_old(50)
# print(student_1.get_name)
 """


""" from datetime import date
class Student:
    #this names as "constructor"
    def __init__(self,name ,age):
        self.age = age
        self.name = name

    def describe(self):
        print(f"Name: {self.name} , Age: {self.age}")


    #class method "decorator" let me modify the behavior of function without changing the function 
    #"takes class as a parmater not 'self'"
    @classmethod
    def initFromBirthYear(cls,name,birthYear):
        return cls(name, date.today().year - birthYear)

student1 = Student("islam",20)
student2 = Student.initFromBirthYear('ahmed',1993)
student2.describe() """


""" class pizza:
    def __init__(self,ingredients):
        self.ingredients = ingredients

    @classmethod
    def vegen(cls):
        return cls(["cheese", 'olives', "cucumber"])

    @classmethod
    def meat(cls):
        return cls(["meat", 'cheese',"olives"])

    #dunder"double underscore" function used to customize the output of class
    def __str__(self):
        return f"Pizza ingredients are {self.ingredients}"


pizza1 = pizza(['tomatoes',"loives"])
pizza2 = pizza.vegen()
pizza3 = pizza.meat()

print(pizza1,pizza2,pizza3)
 

dir(pizza) #used to know more about dunder function
 """

""" class Math:

#Static method "can't modify class or self paramter" takes any number of paramter
    @staticmethod
    def add(x,y):
        return x + y

    @staticmethod
    def add5(num):
        return num + 5

    @staticmethod
    def add10(num):
        return num + 10

    @staticmethod
    def Pi():
        return 3.14


x = Math.add(5,10)
y = Math.add5(x)
z = Math.add10(y)
print(x,y,z) """

""" class pizza:
    def __init__(self,radius,ingredients):
        self.ingredients = ingredients
        self.radius = radius

    def __str__(self):
        return f"Pizza ingredients are {self.ingredients}"

    def area(self):
        return pizza.circle_area(self.radius)

    #we can use it for non class functions
    @staticmethod
    def circle_area(r):
        return r ** 2 * 3.14   #PI

p = pizza(6,["tom","jom"])
print(p.area())
print(pizza.circle_area(4)) """

""" #Inheritance
class Person:
    def __init__(self,name , age):
        self.name = name
        self.age = age

    def display(self):
        return f"name is {self.name} and age is {self.age}"
        
class Man(Person):
    gender = "Male"
    no_of_men = 0

    def __init__(self, name, age,voice):
        #paramter to inherit
        super().__init__(name, age)
        self.voice = voice
        Man.no_of_men += 1

    def display(self):
        string = super().display()
        return string + f" and voice is {self.gender} and voice {self.voice}"
    

man = Man("Mahmoud",23,"loud")
print(man.display())
#to check inheritance
print(isinstance(man,Person)) """


""" #Abstraction
from abc import ABC,abstractmethod

class Shape(ABC):
    #abstract used here to map the parent class for every child
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def permimeter(self):
        pass


class Square(Shape):
    def __init__(self,side):
        self.__side = side


    def area(self):
        return self.__side * self.__side

    def permimeter(self):
        return self.__side *4

class Rect(Shape):
    def __init__(self,length , width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def permimeter(self):
        return (self.__length + self.__width) * 2

square = Square(10)
print(f"{square.area()} and {square.permimeter()}") """


""" class Man:
    def __init__(self,name , age):
        self.name = name
        self.age = age

    #used to add paramters "self refer to first object ofther refer to second obj"
    def __add__(self,other):
        names = self.name + "and" + other.name
        ages = self.age + other.age
        return f"names {names}  sum of ages: {ages}"

    #less than to compare if less than
    def __lt__(self,other):
        return self.age < other.age

    def display(self):
        return f"name is {self.name} and age is {self.age}"
      
man = Man("islam", 20)
man2 = Man("ahmed",30)

print(man+man2)
print(man<man2) """
