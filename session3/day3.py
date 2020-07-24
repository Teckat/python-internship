#  numpy


#  importing numpy

import numpy as np

# arr = np.array([1, 2, 3, 4, 5])

# print(arr)


# numpy version check

# print(np.__version__)


#  Type() of array

# print(type(arr))


#  Dimensions of Arrays

#  1. 0-D Arrays

# arr = np.array(23)

# print(arr)

#  2. 1-D Array

# arr = np.array([1, 2, 3, 4, 5, 6])
# print(arr)

# 3. 2-D Arrays

# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr)


# 4. 3-D Arrays

#  [1,2,3,4,5,6]
#  [7,8,9,10,11,12]

#  [13,14,15,16,17]
#  [18,19,20,21,22]

# arr = np.array([[[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]],
#                 [[13, 14, 15, 16, 17], [18, 19, 20, 21, 22]]])


# print(arr)


# checking dimension of array

# arr = np.array([[[1, 2, 3, 4, 5], [7, 8, 9, 10, 11]],
#                 [[13, 14, 15, 16, 17], [18, 19, 20, 21, 22]]])

# print(arr.ndim)


# Indexing if Arrays

#  accessing data from 1-D array

# arr = np.array([1, 2, 3, 4, 5])

# print(arr[3])

# Accessing data from 2-D array
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]


# arr = np.array([[1, 2, 3, 4, 5], [1, 2, 6, 4, 5]])

# print(arr[1, 2])

# add numbers in an array

# arr = np.array([[1, 2, 3, 4, 5], [1, 2, 6, 4, 5]])

# print(arr[0, 1]+arr[1, 1])


# accessing data from a 3-D array

# arr = np.array([[[1, 2, 3, 4, 5], [7, 8, 9, 10, 11]],
#                 [[13, 14, 15, 16, 17], [18, 19, 20, 21, 22]]])

# print(arr[0, 1, 3])


# negative index

#


# arr = np.array([[1, 2, 3, 4, 5], [12, 13, 14, 15, 16]])

# print(arr)
# print(arr[1, -2])


#  slicing

#  numpy slicing
# 1. [start:end]
# 2. [start:end:step]
# 3. [:end] starts by default from 0th position
# 4. [start:] give you data till end position
