#  class and object (oops concept)


class class_8:
    print()
    name = 'amar'


# class class_9:
#     name = 'rahul'
#     age = 23

#     def welcome(self):
#         print("welcome to teckat")

# # a = class_9()   # create object of class abc
# # b = class_8()

# # c = class_9()

# # # print(abc.name)  # accessing attribute through class

# # print(a.name)   # accessing through object of the class
# # print(b.name)
# # print(c.age)


# a = class_9()

# a.welcome()


# constructor __init__

# class student:

#     def __init__(self, name, age):
#         print("hello")

#         self.name = name
#         self.age = age

#     def modify_name(self, name):
#         self.name = name


# a = student('amar', 12)

# print("before modifying", a.name, a.age)

# a.modify_name('john')

# print("after modifying", a.name, a.age)


class student:

    def __init__(self):
        self.name = ''
        self.age = 0

    def input_details(self):
        self.name = input('Enter name')
        self.num1 = int(input('Enter 1st marks'))
        self.num2 = int(input('Enter 2nd marks'))

    def add(self):
        self.total = self.num1+self.num2

    def print_details(self):
        print("name = ", self.name)
        print("totla marks = ", self.total)


a = student()

a.input_details()
a.add()
a.print_details()


# special attributes


# 1. getattr()
# accessing attributes usin getattr()
print("name (getattr) = ", getattr(a, 'name'))


# 2. hasattr()

print("hasattr(age) = ", hasattr(a, 'age'))
print("hasattr(salary) = ", hasattr(a, 'salary'))


# 3. setattr()

setattr(a, 'name', 'amar')

print("setattr(name=amar) = ", a.name)


#  4. delattr()

delattr(a, 'name')

print("delattr(name) = ", a.name)
