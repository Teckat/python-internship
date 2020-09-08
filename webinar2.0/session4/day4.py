# dobble game

# 1. two set of datas
# 2. there will be characters
# 3. find the common match

# ['a','b','c','d']
# ['c','z','x','r']

import string
import random


l1 = []
l2 = []
l3 = []

sample = list(string.ascii_letters)

# print(sample)

# chose a common character out of sample

m = random.choice(sample)

#  remove the chosen sample from the list of sample
sample.remove(m)

# print(m)
# print(sample)


# choosing a position in both the list
pos1 = random.randint(0, 14)
pos2 = random.randint(0, 14)
pos3 = random.randint(0, 14)

# print(pos1, pos2)


for i in range(15):

    if(i != pos1 and i != pos2 and i != pos3):

        s = random.choice(sample)
        l1.append(s)
        sample.remove(s)

        s = random.choice(sample)
        l2.append(s)
        sample.remove(s)

        s = random.choice(sample)
        l3.append(s)
        sample.remove(s)
    elif(i == pos1 and i == pos2 and i == pos3):
        l1.append(m)
        l2.append(m)
        l3.append(m)

    elif(i == pos1 and i == pos2):  # pos1=pos2, pos2=pos3, pos3=pos1

        l1.append(m)
        l2.append(m)

        s = random.choice(sample)
        l3.append(s)
        sample.remove(s)

    elif(i == pos2 and i == pos3):

        l2.append(m)
        l3.append(m)

        s = random.choice(sample)
        l1.append(s)
        sample.remove(s)

    elif(i == pos3 and i == pos1):

        l3.append(m)
        l1.append(m)

        s = random.choice(sample)
        l2.append(s)
        sample.remove(s)

    elif(i == pos1):
        l1.append(m)

        s = random.choice(sample)
        l2.append(s)
        sample.remove(s)

        s = random.choice(sample)
        l3.append(s)
        sample.remove(s)

    elif(i == pos2):
        l2.append(m)

        s = random.choice(sample)
        l1.append(s)
        sample.remove(s)

        s = random.choice(sample)
        l3.append(s)
        sample.remove(s)

    elif(i == pos3):
        l3.append(m)

        s = random.choice(sample)
        l1.append(s)
        sample.remove(s)

        s = random.choice(sample)
        l2.append(s)
        sample.remove(s)

print(l1)
print(l2)
print(l3)

choice = input('enter the common character')

if(choice == l1[pos1]):
    print('correct answer')
else:
    print('wrong answer')
