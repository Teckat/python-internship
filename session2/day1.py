#  operator and assignments

#  1. arithmetic operator  2. logical operator  3. comparison operator

# 1. arithmetic operator

#  1. + addition

a = 2+3

print("addition = ", a)

# 2. subtraction
#
a = 3-2
print("subtraction = ", a)

# 3. multiplication

a = 3*2
print("multiplication = ", a)


# 4. Division

a = 5/2
print("division = ", a)


#  5. % Modulo

a = 5 % 2
b = 4 % 2
print("remainder a = ", a, "\nremainder b = ", b)


# 6. ** exponential

a = 5**2

print("exponential = ", a)


# 7. floor Division
#  method 1 to convert integer

a = int(5/2)
print("method 1 = ", a)

# method 2 using floor division

a = 5//2
print("floor division method = ", a)


#  8. unary operator

a = 3

print("+a = ", +a)
print("-a = ", -a)

print("manual conversion = ", -1*a)


# example

a = 10/4  # 2.5  -> 2 or 3
a = 10//4  # 2

a = 10 // -4  # -2 or -3   o/p -> -3

a = -10//-4  # 2


#  2. comparison operator:-

#    <                                   <=          !=           >=                                   >
# [less]===========================================|exact|==========================================[greater]
#                                                    ==


a = 9000
b = 900

c = int(a == b)

print("exactly match = ", a == b, c)
print("not exact match = ", a != b)
print("less than exact match = ", a < b)
print("greater than exact match = ", a > b)
print("less than equal exact match = ", a <= b)
print("greater than equal exact match = ", a >= b)


#  3. logical operator

#  1. not

print("not = ", not True)


#  2. and


print("and = ", 2 < 3 and 3 < 4 and 5 > 6)


#  3. or opearator

print("or = ", 3 < 4 or 3 > 4 or 5 > 6)

a = 16
b = 8

print("manual <= ", a < b or a == b)
