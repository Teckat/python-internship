#  control structure

#  1. if else elif

# if condition:
# codes -----
# ------------
# ----------

# a = 0

# if (a > 0):
#     print("a > 0")
#     print("the value = ", a)

# elif(a < 3):
#     print("a<3")

# elif (a == 0):
#     print("a==0")

# else:
#     print("a < 0")


# take input from the user and print even or odd

# a = int(input('Enter a number'))

# print(a, type(a))

# if(a % 2 == 0):
#     print("the number is even")

# elif(a % 2 != 0):
#     print("the number is odd")

# else:
#     print("the number is odd")


#  multiple inputs

# method 1
# a = input('enter first name')
# b = input('enter second name')

# c = int(input('enter your age'))
# print(a, b, " age = ", c)

# # concatenation of string

# print(a+" "+b+" age = "+str(c))


# 2. for loop()

# print 0 to 5

# for i in range(6):
#     print(i)


# print 1 to 5

# for i in range(1, 6):
#     print(i)

# print 1 to 5 with 2 incrementation

# for i in range(1, 6, 2):
#     print(i)

#  using loop() with list

# l = [4, 5345, 6, 54, 21, 53]

# # method 1
# # for i in range(len(l)):
# #     print(l[i])

# # method 2

# for i in l:
#     print(i)


#  split() function
# 12 13 54

# a = input("enter multiple numbers using spaces").split(" ")
# b = []
# print(a, type(a))

# for i in a:
#     b.append(int(i))

# print(b)


# 3. while loop

# c = 'y'

# while c == 'y':

#     c = input('enter y to continue or x to quit')


c = ((2.56 * 10**5)+(5.22 * 10**4)*5)*10
print(c)
