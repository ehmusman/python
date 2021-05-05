
# ------------------------------ Creating Class ------------------------

# class Point:
#     def draw(self):
#         print("Draw")


# point = Point()
# print(type(point))

# print(isinstance(point, Point))
# print(isinstance(point, object))
# print(isinstance(Point, object))

# object is a base class for all the custom or built in classes like prototypical object in JS

# ------------------------------ Constructor ------------------------


# class Point:
#     def __init__(self, x, y):  # constructor function
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# point = Point(1, 2)
# point.draw()
# print(point.x)


# ------------------------------ Class vs instance attributes ------------------------

# class Point:
#     default_color = "Green"
#     def __init__(self, x, y):  # constructor function
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# point = Point(1, 2)
# point.draw()
# # we can add new attributes in this point object
# # these are instance attributes. these are only specific to a specific instance of a class
# # 
# point.z = 10
# print(point.x, point.z) # z will be printed

# point1 = Point(3, 4)
# print(point1.x) # error while printing z
# point1.draw()

# # Similarlhy we have class attributes. these attributes will be globally available for all the instances of that class
# # Below are the class attributes and can be accessed by any instances or class itself
# # if we'll change the value of class attribute, this change will be visible for all the instances and class itself
# print(point.default_color)
# print(point1.default_color)
# print(Point.default_color)



# ------------------------------ Class vs instance Methods ------------------------

# class Point:
#     def __init__(self, x, y):  # constructor function
#         self.x = x
#         self.y = y

#     @classmethod
#     def zero(cls): # this is factory method
#         return cls(0, 0)

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# # Class method i accessible from class level. we can use it to generate the new class instances with some default values. like we are initializing the class instance with 0, 0

# point = Point.zero()
# point.draw()




# ------------------------------ Magic Methods ------------------------

# these methods are called by python interprator automatically
#  these are surrounded by double underscore

# class Point:
#     def __init__(self, x, y):  # constructor function
#         self.x = x
#         self.y = y
#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")
#     def __str__(self):
#         return f"({self.x}, {self.y})"


# point = Point(3,4)
# # following both are returning same
# print(point.__str__())
# print(str(point))


# ------------------------------ Comparison Objects ------------------------


# class Point:
#     def __init__(self, x, y):  # constructor function
#         self.x = x
#         self.y = y
#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#     def __eq__(self, other): # to check the equality of two objects
#         return self.x == other.x and self.y == other.y
#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y


# point = Point(4,5)
# other = Point(3,4)

# print(point == other)
# print(point > other)
# print(point < other)

# ------------------------------ Performing Arithmatic Operations ------------------------



# class Point:
#     def __init__(self, x, y):  # constructor function
#         self.x = x
#         self.y = y
#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#     def __eq__(self, other): # to check the equality of two objects
#         return self.x == other.x and self.y == other.y
#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)

# point = Point(4,5)
# other = Point(3,4)

# combined = point + other
# print(combined.x, point + other)

# ------------------------------ Making Custom Container ------------------------

# class TagCloud:
#     def __init__(self):
#         self.tags = {}
    
#     def add(self, tag):
#         self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1
#     def __getitem__(self, tag):
#         return self.tags.get(tag.lower(), 0)
#     def __setitem__(self, tag, count):
#         self.tags[tag.lower()] = count
#     def __len__(self): # to get the length
#         return len(self.tags)
#     def __iter__(self):
#         return iter(self.tags)


# cloud = TagCloud()
# cloud.add("python")
# cloud.add("Python")
# cloud.add("python")
# cloud.add("JS")
# cloud.add("JS")
# print(cloud.tags)

# tags_count = cloud["python"]
# print(tags_count)
# cloud["python"] = 10
# tags_count = cloud["python"]
# print(tags_count)

# print(len(cloud))

# for tag in cloud:
#     print(tag)


# ------------------------------ Private Members  ------------------------

# class TagCloud:
#     def __init__(self):
#         self.__tags = {}
    
#     def add(self, tag):
#         self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1
#     def __getitem__(self, tag):
#         return self.__tags.get(tag.lower(), 0)
#     def __setitem__(self, tag, count):
#         self.__tags[tag.lower()] = count
#     def __len__(self): # to get the length
#         return len(self.__tags)
#     def __iter__(self):
#         return iter(self.__tags)


# cloud = TagCloud()
# cloud.add("python")
# cloud.add("Python")
# cloud.add("python")
# cloud.add("JS")
# cloud.add("JS")
# # print(cloud.__tags)

# tags_count = cloud["python"]
# print(tags_count)
# cloud["python"] = 10
# tags_count = cloud["python"]
# print(tags_count)

# print(len(cloud))

# for tag in cloud:
#     print(tag)

# # there is a problem in this implementation. if we get any tag with previous approach, we'll get 0 if tag not exists and any number when tag exists. if we'll get the tag directly from instance attribute, the program will be crashed.
# # we face keyError
# # print(cloud.__tags["tag"])

# # after adding __ before tags attribute, we'll face AttributeError
# # print(cloud.__tags)

# # in oython there is no concept of private members. we can still access the __tags. but the direct access is not possible

# # double underscore is only a restriction to access the private members. we can still access it in following way
# # print(cloud.__dict__)
# # print(cloud._TagCloud__tags["python"])



# ------------------------------ Properties  ------------------------

# class Product:
#     def __init__(self, price):
#         self.set_price(price)
#     def get_price(self):
#         return self.__price
#     def set_price(self, value):
#         if value <= 0:
#             raise ValueError("Price must be greater than 0")
#         self.__price = value


# # the problem is that we can set the negative price to above class instance.
# # to prevent it we need to add getter and setter function

# product = Product(20)
# print(product.get_price())
# # above implementation is not pythonic. means not best practices that should be used inpython






# class Product:
#     def __init__(self, price):
#         self.__set_price(price)
#     def __get_price(self):
#         return self.__price
#     def __set_price(self, value):
#         if value <= 0:
#             raise ValueError("Price must be greater than 0")
#         self.__price = value
    

#     price = property(__get_price, __set_price)


# # the problem is that we can set the negative price to above class instance.
# # to prevent it we need to add getter and setter function

# product = Product(20)
# product.price = 120
# print(product.price)
# # above implementation is not pythonic. means not best practices that should be used inpython
# # we make the getter and setter methods to private. but it'll create a noisy code. we have a better approach



# class Product:
#     def __init__(self, price):
#         self.price = price

#     @property
#     def price(self):
#         return self.__price
    
#     @price.setter
#     def price(self, value):
#         if value <= 0:
#             raise ValueError("Price must be greater than 0")
#         self.__price = value
    

# # with the decorators, the code is more cleaner.
# # if we remove the code of @price.setter, the price attribute will become a readonly. we'll not be able to overwrite it after initializing

# product = Product(20)
# product.price = 120
# print(product.price)




# ------------------------------ Inheritance  ------------------------

# class Animal: 
#     def __init__(self):
#         self.age = 1

#     def eat(self):
#         print("eat")


# # Animal is Parent, Base class
# # Mammal is Child or Sub class
# class Mammal(Animal): 
#     def walk(self):
#         print("walk")


# class Fish(Animal):
#     def swim(self):
#         print("swim")


# fish = Fish()
# fish.eat()
# m = Mammal()
# m.walk()
# print(m.age)


# ------------------------------ The Object Class  ------------------------

# class Animal: 
#     def __init__(self):
#         self.age = 1

#     def eat(self):
#         print("eat")


# class Mammal(Animal): 
#     def walk(self):
#         print("walk")


# class Fish(Animal):
#     def swim(self):
#         print("swim")


# fish = Fish()
# m = Mammal()
# # Some usefull methods
# print(isinstance(m, Mammal))
# print(isinstance(m, Animal))
# print(isinstance(m, object))
# print(isinstance(Mammal, object))



# print(issubclass(Mammal, Animal)) # True
# print(issubclass(Animal, object)) # True
# print(issubclass(Mammal, object)) # True
# print(issubclass(Animal, Mammal)) # False



# ------------------------------ Method Overriding  ------------------------

# class Animal: 
#     def __init__(self):
#         self.age = 1
#         print("Animal Constructor")

#     def eat(self):
#         print("eat")


# class Mammal(Animal): 
#     def __init__(self):
#         super().__init__()
#         print("Mammal Constructor")
#         self.weight = 1

#     def walk(self):
#         print("walk")

# m = Mammal()
# print(m.age) # the constructor of Animal class is over riding by the constructor of Mammal class. so m.age is raising error. we nee to initialize the Animal constructor also


# ------------------------------ Multi level inheritance  ------------------------
# we need to avoid the multi level inheritance. we need to only stick with maximum one or two level. it can create problem,
# it can create complexity in our program. We dont need to develop the universe and don't need to solve the problems that never exists.
# it's a bad when we dont use it properly
# class Animal:
#     def eat(self):
#         print("Eat")

# class Bird(Animal):
#     def fly(self):
#         print("Fly")


# class Chicken(Bird):
#     pass

# here the problem is that chicket don't fly. so multilevel inheritance introduced a problem.


# ------------------------------ Multiple inheritance  ------------------------

# class Employee:
#     def greet(self):
#         print("Employee Greet")

# class Person:
#     def greet(self):
#         print("Person Greet")

# class Manager(Employee, Person):
#     pass
# m = Manager()
# m.greet() # it'll return Employee Greet. 
# when we invoke a method of any class instance, if this m ethod is not exists in that class, the python compiler will search the method in it's first parent class. if it found, it'll be printed.
# so in future if any person changed the order of Manager parent classes, the code behaviour will be changed

# A Good example of multiple inheritance.

# class Flyer:
#     def fly(self):
#         pass

# class Swimmer:
#     def swim(self):
#         pass

# class FlyingFish(Flyer, Swimmer):
#     pass
# we can use multiple inheritance, if methods are different in all parent classes.




# ------------------------------ A Good Example inheritance  ------------------------

# class InvalidOperationError(Exception):
#     pass

# class Stream:
#     def __init__(self):
#         self.opened = False
#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already open")
#         self.opened = True
#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is already closed")
#         self.opened = False

# class NetworkStream(Stream):
#     def read(self):
#         pass

# class FileStream(Stream):
#     def read(self):
#         pass



# ------------------------------ Abstract Base Classes  ------------------------

# from abc import ABC, abstractmethod
# # with above module we'll make the Stream class an abstract class whose instance can't be created. and abstractmethod is enforcing that in child classes it's must to create a read method. if we'll not create that method, the child class will also become an abstract class whose instance can't be created. and if in child class we add a method other than read, it'll again raise an error. this is for our type safety

# # abstract clases behave like an interface. that make sure the sub classes should have predefined methods and attributes to streamline the development

# class InvalidOperationError(Exception):
#     pass

# class Stream(ABC):
#     def __init__(self):
#         self.opened = False
#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already open")
#         self.opened = True
#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is already closed")
#         self.opened = False
    
#     @abstractmethod 
#     def read(self):
#         pass

# class NetworkStream(Stream):
#     def read(self):
#         pass

# class FileStream(Stream):
#     def read(self):
#         pass

# # stream = Stream() # it's not allowed with abstract classes.



# ------------------------------ Polymorphism  ------------------------
# from abc import ABC, abstractmethod

# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass


# class DropDownList(UIControl):
#     def draw(self):
#         print("Draw Drop Down List")

# class TextBox(UIControl):
#     def draw(self):
#         print("Draw Textbox")


# def draw(control):
#     # Following function will behave differently according to the instance of differenct classes
#     control.draw()


# ddl = DropDownList()
# tb = TextBox()

# draw(tb)

# ------------------------------ Duck Typing  ------------------------
# it's a programming style that does not look at the Object's type to determine if it has right interface.
# in polymorphism example, we used following function. here no body knows what is the type of control parameter. if this will be a dictionary and have draw method, that draw method will be invoked. if it'll be a list, a loop can be implemented. python will be happy if a specific type of operation is implemented like if draw method exists, it'll be invoked. otherwise python will spit an error 

# def draw(control):
#     control.draw()




# ------------------------------ Extensing built in classes  ------------------------

# class Text(str):
#     # following new method is added in str build in methods
#     def duplicate(self):
#         return self + self


# text = Text("Python")
# print(text.duplicate())

# class TrackableList(list):
#     def append(self, val):
#         print("Append Called")
#         super().append(val)

# list = TrackableList()
# list.append("1")

# ------------------------------ Data Classes  ------------------------

# Sometime we use classes only to store data. these classes dont have any method attributes.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y



p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2)
# build in id method provides the memory location of objects
print(id(p1))
print(id(p2))

# if we have only data clases with nno method or behaviour. we can use namedtuple instance

from collections import namedtuple

Pointt = namedtuple("Pointt", ["x", "y"])

p1t = Pointt(x=1, y=2)
p2t = Pointt(x=1, y=2)

# We don't need to implement the magic method for this
print(p1t == p2t)
print(id(p1t))
print(id(p2t))
# namedtuple are immutable. we cant change the value after initializing it. we need to again create new variable if we want to modify the previous one. mean overriding the previous one