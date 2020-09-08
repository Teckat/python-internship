#  inheritance

# Single inheritance


# class student:  # base class

#     def hello(self):
#         print("Welcome")


# class curricular(student):    # derived class

#     def subject(self):
#         print('maths')


# # a = student()
# # a.hello()

# b = curricular()
# b.subject()
# b.hello()


#  Multiple Inheritance

#  multiple base classes but only 1 derived class

# class student:

#     def stud_details(self):

#         self.name = input('enter name')

#     def display(self):
#         print("name = ", self.name)


# class parent:

#     def parent_details(self):
#         self.pname = input("enter parent's name")

#     def display_parent(self):
#         print("parent's name = ", self.pname)

# method 1

# a = student()
# b = parent()

# a.stud_details()
# b.parent_details()

# a.display()
# b.display_parent()

# multiple inheritance method


# class main(student, parent):

#     def heading(self):
#         print("details of the student")


# a = main()

# a.stud_details()
# a.parent_details()

# a.heading()
# a.display()
# a.display_parent()


# inheriting constructors from base class to derived class

# class student():

#     def __init__(self):
#         print("constructor of student")


# class parent():

#     def __init__(self):
#         print("constructor of parent")


# class main(student, parent):

#     def __init__(self):
#         print("constructor of main")

#         student.__init__(self)
#         parent.__init__(self)


# a = main()


#  encapsulation

# class student:

#     name = 'amar'
#     __age = 12

#     b = __age


# a = student()

# print("name = ", a.name)
# print("Age(b) = ", a.b)
# print("Age = ", a.age)


# ======================================================================================================

#  FIZZ BUZZ GAME
# INPUT A SET OF NUMBERS IN A LIST BY USER
# MULTIPLE OF 3 – FIZZ
# MULTIPLE OF 5 – BUZZ
# MULTIPLE OF 15 - FIZZBUZZ


a = input('enter 3 numbers').split()

print(a)

for i in a:

    if(int(i) % 15 == 0):
        print("FIZZBUZZ")
    elif(int(i) % 3 == 0):
        print("FIZZ")

    elif(int(i) % 5 == 0):
        print("BUZZ")
