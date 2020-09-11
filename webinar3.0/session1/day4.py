#  slicing

a = "welcome to india"

x = a[0:10]
# print(x)

# print(a[11:])


# print(a[:9])

# print(a[5:10])

# print(a[0:-2])

# print(a[::-1])

# print(len(a))

# list

# l = [1, 2, 3, 45, 6, 7, 78, 789]

# print(l)

# l = ['abc', 'cde', 'efg']
# print(l)

# l = [1, 2, 3, 45, 'abc', 'cde', 'efg']
# print(l)

# print(l[0])


# 1. append()

# l.append('hfg')
# print(l)

# a = [1, 2, 34, 5]

# l.append(a)

# print(l)

# l.append(54)
# print(l)


# # extend()

# l.extend(a)
# print(l)

# print(l[0], l[3], l[-1])


l = ['abc', 'cde', 'efg', 'abc']
print('original list : ', l)
# slicing

# print(l[0:len(l)])

# x = l[::-1]
# print('slicing reverse : ', x)
# print('original list after reverse slicing : ', l)

# # reverse()
# l.reverse()
# print('reverse list using reverse function : ', l)

# insert()

# l.insert(1, 'hjp')
# print(l)

# count()

# x = l.count('abc')
# print(x)

# remove()

# l.remove('abc')
# print(l)

#  pop ()
# l.pop(2)
# print(l)

# sort()

l.sort()
print(l)
l.reverse()
print(l)

# clear()

l.clear()
print(l)


# del

del l

print(l)
