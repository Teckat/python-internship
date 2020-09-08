#  slicing of numpy


import numpy as np

#  numpy slicing
# 1. [start:end]
# 2. [start:end:step]
# 3. [:end] starts by default from 0th position
# 4. [start:] give you data till end position


# 1.  [start:end]


# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])


# print(arr[1:7])


# 2. [start:end:step]

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 22, 13, 34,
#                 78, 55, 667, 75, 42, 31, 34456, 4, 3, 5556])

# print(arr[1:24:5])


# 3. [:end] starts by default from 0th position

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 22, 13, 34,
#                 78, 55, 667, 75, 42, 31, 34456, 4, 3, 5556])

# print(arr[:10])

# 4. [start:] give you data till end position

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 22, 13, 34,
#                 78, 55, 667, 75, 42, 31, 34456, 4, 3, 5556])

# # print(arr[3:])
# print(arr[:: 3])


#  2-D slicing :


arr = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])

print(arr)

print(arr[1, 2:5])
