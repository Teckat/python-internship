
#  Sequence

# 2. List

l = [1, 2, 3, 4]

print("original data = ", l)

#  1. append()

# example 1
l.append(5)
print("append() = ", l)

# example 2

a = ['a', 'b', 'c']
l.append(a)
print("append list l = ", l)

# indexing

# print first element of list l
print("indexing = ", l[0])
print("indexing = ", l[5])

# 2. extend()
z = [45, 67, 89, 90, 23]

z.extend(a)
print("extend z = ", z)

#  indexing
print("indexing = ", z[5])
print("reverse indexing = ", z[-2])

# slicing

l = [1, 2, 3, 'a', 'b', 'teckat']

print("slicing = ", l[0:3])

# 3. length

print("length = ", len(l))

# 4. insert(i, x)

l.insert(4, 20)
l.insert(2, 98)
l.insert(5, "welcome")
print("insert() = ", l)

# 5. count()

a = [1, 2, 3, 1, 2, 5, 7, 9, 20, 1]
print("list a = ", a)
print("count(1) = ", a.count(1))

#  6. remove()  remove an element using value

a.remove(1)
print("remove(1) = ", a)

# 7. pop() remove an element using position
a = [1, 2, 3, 1, 2, 5, 7, 9, 20, 1]

a.pop(5)
print("pop() = ", a)


# 8. reverse()

# method1
a = [1, 2, 3, 1, 2, 5, 7, 9, 20, 1]
a.reverse()
print("reverse() = ", a)

# method 2
a = [1, 2, 3, 1, 2, 5, 7, 9, 20, 1]
l = a[::-1]
print("original list a = ", a)
print("reverse slicing method = ", l)

# 9. sort()

# sort in ascending order
a.sort()
print("ascending sort = ", a)

# sort in descending order

print("descending sort = ", a[::-1])


# 10. copy()
a = [1, 2, 3, 1, 2, 5, 7, 9, 20, 1]
l = a.copy()

a.reverse()
print("l = ", l)
print("a = ", a)

# 11. clear()

a.clear()

print("l = ", l)
print("a after clear = ", a)

# 13. del

del a

# print("a after del = ", a)


#  sequence

# 3. tuple()

t = (12, 34, 56, 78, 'a')

print(type(t), t)
