# class human:
#     age = 35
#     name = "amar"

#     def update_age(self,age):
#         print(self.age)
#         self.age = age

#         print(self.age)
#         print(age)


# hmn = human()
# # hm1 = human()
# # print(hmn.name)
# # print(human.age)

# hmn.update_age(48)


#  constructor

class human():

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def add(self):
        self.age = self.age+10


hmn = human(12, 'john')
# hmn.add()
# print(hmn.age)

abc = "name"


# getattr
# print(getattr(hmn, abc))
# print(hmn.name)


#  hasattr

# print(hasattr(hmn, "sal"))

# setattr
print(hmn.name)
setattr(hmn, "name", "amar")
print(hmn.name)


# delattr

print(hmn.age)
delattr(hmn, "age")
print(hmn.age)
