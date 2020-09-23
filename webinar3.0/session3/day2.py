
# inheritance

# 1. simple inheritance


# class fruit():

#     banana = 12

#     def __init__(self):
#         self.b = self.banana

#     def mango(self):
#         print("mango")


# class apple(fruit):
#     apple = 5


# f = fruit()

# print(f.apple)

# a = apple()
# print(a.apple)
# print(a.banana)

# print(a.b)


# 2. multiple inheritance

# class a():
#     def __init__(self):
#         print("constructor of a")


# class b():
#     def __init__(self):
#         print("constructor of b")


# class d(a, b):
#     def __init__(self):
#         print("constructor of c")

#         b.__init__(self)
#         a.__init__(self)


# test = d()

# encapsulation

# class abc():
#     __name = "ram"


# test = abc()

# print(test.__name)

# fizzbuzz

a = input('enter three numbers').split()
b = []
for i in a:
    b.append(int(i))

print(b)

for i in b:

    if(i % 15 == 0):
        print("fizzbuzz")
    elif(i % 5 == 0):
        print("buzz")
    elif(i % 3 == 0):
        print("fizz")
