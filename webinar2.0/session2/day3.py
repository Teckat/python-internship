# functions

#  syntax


# def print_hello():     # function defination
#     print("hello")
#     print("hello")
#     print("hello")
#     print("hello")
#     print("hello")


# print_hello()   # function call


# types of functions

#  1. no parameter no return
#  2. with parameter no return
#  3. no parameter with return
#  4. with parameter with return


# create a function to add 2 nos

# 1. no parameter no return

# def sum():
#     a = 8
#     b = 9

#     s = a+b
#     print("sum = ", s)


# sum()

# 2. with parameter no return

# def sum(c, d):

#     s = c+d
#     print("sum = ", s)


# a = 8
# b = 9
# sum(a, b)

# 3. no parameter with return

# def sum():

#     a = 8
#     b = 9
#     s = a+b
#     return(s)


# s = sum()
# print("sum = ", s)


#  4. with parameter with return

# def sum(a, b):

#     s = a+b
#     return(s)


# a = 8
# b = 9

# s = sum(a, b)
# print("sum = ", s)


# find the maximum number out of 10 nos

# def convert_int(number):
#     num = []
#     for i in number:
#         num.append(int(i))
#     return num


# number = input('enter 10 numbers using commas').split(',')

# print("number = ", number)

# number = convert_int(number)

# print("number = ", number)

# number.sort()

# print("sorted num list = ", number)

# print("largest value = ", number[len(number)-1])


# take 10 numbers from the user and ask him the choice to do with the number
# 1 -> maximum value
# 2 -> second maximum value
# 3 -> print even numbers list
# 4 -> print odd numbers list

def convert_int(numbers):
    num = []
    for i in numbers:
        num.append(int(i))
    return(num)


def maxValue(numbers):
    numbers.sort()
    print("max value = ", numbers[-1])


def secondMaxValue(numbers):
    numbers.sort()
    print("max value = ", numbers[-2])


def evenList(numbers):

    l = []
    for i in numbers:

        if(i % 2 == 0):
            l.append(i)
    print("even list = ", l)


def oddList(numbers):

    l = []
    for i in numbers:

        if(i % 2 != 0):
            l.append(i)
    print("odd list = ", l)


numbers = input('enter 10 numbers seperated with commas').split(',')

numbers = convert_int(numbers)

choice = int(input(' enter your choice'))

if (choice == 1):
    maxValue(numbers)

elif(choice == 2):
    secondMaxValue(numbers)

elif(choice == 3):
    evenList(numbers)

elif(choice == 4):
    oddList(numbers)

else:
    print("enter a correct choice value")
