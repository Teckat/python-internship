# 3. tuple

# t = (1, 2, 4, 56, 78)
# print("tuple = ", t)

# # 1. indexing

# l = []
# l.append(t[0])
# l.append(t[1])
# l.append(t[2])

# print("indexing = ", t[1])

# print("tuple elemets transfered to list", l)
# print("original tuple", t)

# # 2. slicing

# print("slicing method 1 = ", t[1:len(t)])
# print("slicing method 2 = ", t[1:])

# #  3. Delete

# del t
# # print(t)

# # 4. count()
# t = (1, 2, 3, 2, 45, 67, 2)

# print("count(2) = ", t.count(2))


# =================================================================================================

# 4. dictionary

d = {}

print(" empty dictionary = ", d, type(d))

# creating and inserting values in dictionary

d = {1: 'amar', 2: 'akbar', 3: 'anthony'}

print("values of dictionary = ", d)

# getting values against the key

print("d[1] = ", d[1])

# multiple values against one key

d = {
    1: ['amar', 'hello', 'teckat', 189022345],
    2: 'akbar',
    3: 'anthony'
}

print("multiple values against single key = ", d)
print("d[1] = ", d[1])
print("d[1][1] = ", d[1][1])


#  finding keys

print("keys() = ", d.keys())

# finding values

print("values() = ", d.values())


# modifying values

d = {1: 'amar', '2': 'akbar', 3: 'anthony'}

d[1] = 'teckat'
print("key present value changed = ", d)

d[2] = 'hello'

print("key not present", d)

# copy()

nd = d.copy()

print("copy() = ", nd)


#  pop()
d = {1: 'amar', '2': 'akbar', 3: 'anthony'}

d.pop('2')

print("pop('2') = ", d)

# update()

d = {1: 'amar', '2': 'akbar', 3: 'anthony'}
t = {1: 'school', 2: 'college', '3': 'student', 3: 'teacher'}

d.update({3: 'shyam'})

print('dictionary after update() = ', d)

# ex-1
d.update(t)

print("merging two dictionaries", d)


d = {1: 'amar', '2': 'akbar', 3: 'anthony'}
t = {1: 'school', 2: 'college', '3': 'student', 3: 'teacher'}

# ex-2
t.update(d)

print("t parent and d merger = ", t)


# delete a key

del d[1]
print("after deleting the key", d)

# delete dictionary

del d

# print(d)


#  clear()
d = {1: 'amar', '2': 'akbar', 3: 'anthony'}

print("before clear() = ", d)
d.clear()
print("after clear() = ", d)
