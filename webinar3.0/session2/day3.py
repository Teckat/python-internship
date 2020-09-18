# functions


# def add():
#     s = 2+3
#     print(s)


# add()

# user input

# x = int(input('enter 1st number'))
# y = int(input('enter 2nd number'))

# print(x, type(x))

# z = input('enter 3 numbers using comma').split(',')
# print(z)


# types of functions
# 1. no argument no return
# 2. with argument no return
# 3. no argument with return
# 4. with argument with return


# 1. no argument no return

# def add():
#     x = int(input('enter 1st numbers'))
#     y = int(input('enter 2nd numbers'))
#     s = x+y
#     print(s)


# add()


#  2. with argument no return


# def add(x, y):
#     s = x+y
#     print(s)

# a = int(input('enter 1st numbers'))
# b = int(input('enter 2nd numbers'))

# add(a,b)
# add(15,17)

# 3. no argument with return

# def add():
#     x = int(input('enter 1st number'))
#     y = int(input('enter 2nd number'))
#     s = x+y
#     return s


# x = add()
# print(x)


# 4. with argument with return

# def add(x, y):
#     s = x+y
#     return s


# a = 16
# b = 12

# a = int(input("enter 1st number"))
# b = int(input("enter 2nd number"))

# x = add(a, b)

# print("value of sum = ", x)


# using scope variables

x = 10
print("in main before add() = "+str(x))


def add():
    global x

    x = 12
    print("inside add() = "+str(x))


add()
print("in main after add() = "+str(x))
