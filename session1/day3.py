# Sequence
# 1. string 2. list  3. dictionary  4. tuple

#  1. string

s = "this is teckat. Welcome to teckat"
print(s)

#  triple quotes to write paragraph
st = '''this is teckat. 
Welcome to teckat '''
print("paragraph triple quotes", st)

#  funtions
# 1. capitalize()

a = "this iS tecKat .Welcome to Teckat"
b = a.capitalize()
print("capitalize", b)

# 2. count()
a = "this iS teckat, Welcome to Teckat"

b = a.count("ec")
print("count function = ", b)

# 3. endswith()

a = "this is teckat, Welcome to Teckat"

print("endswith function = ", a.endswith('kat'))

# 4. startswith()

print("startswith() = ", a.startswith('this iS teckat'))


# 5. index()

# finds the value
print("index() = ", a.index('is'))
# doesn't find the value
# print("index() = ", a.index('z'))


# 6. find()

# finds the value
print("find() = ", a.find('is'))
# doesn't find the value
print("find() = ", a.find('z'))


k = "Teckat WelCome All The PaRtners For ThIr SuppOrt"
c = "HELLO GUYS"
s = "teckat heartily welcomes you"
# 7. islower()

print("islower() = ", s.islower())
print("islower() = ", c.islower())

# 8. isupper(c)

print("isupper() = ", s.isupper())
print("isupper() = ", c.isupper())

# 9. lower()

print("lower() = ", k.lower())

# 10. upper()

print("upper() = ", k.upper())

#  11. swapcase()

print("swapcase() = ", k.swapcase())

# stripping

z = "--------hel-lo--------"
# 12. strip()

print("strip() = ", z.strip('-'))

# 13. l.strip()

print("lstrip() = ", z.lstrip('-'))

# 14. r.strip()

print("rstrip() = ", z.rstrip('-'))

# 15. replace()

r = "this is , a good day"

print('replace() = ', r.replace('good', 'pleasant'))

# 16. split()

l = r.split()
nl = r.split(',')

print("split() = ", l)
print("split(',') = ", nl)

#  17. slicing

print("slicing = ", r[5:11])


# sequence
# 2. List

#  blank list

l = []
print("blank list = ", l)

# number list

l = [1, 2, 34, 5, 23, 5, 6]
print("number list = ", l)

#  string list

l = ['dad', 'mom', 'family']
print("string list = ", l)

# float list

l = [1.2, 3.4, 5.6]
print("float list = ", l)

# mixed list

l = [1, 2, 3.4, 6.8, "apple", "banana"]
print("mixed list = ", l)
