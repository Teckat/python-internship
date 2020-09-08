# pandas
import pandas as pd
import numpy as np


#  Three data structures

#  1. Series     2. Data Frames     3. Panel

#  1. Series
#  1-d , homogeneous array, size immutable


# 2. Data frames
#  2-d, heterogeneous typed columns, size mutable


#  3. panel
#  3-d, size mutable, general 3d labeled


# Series :

# [10, 20, 30, 50, 60]


# pandas.Series(data,index,dtype,copy)

# datas accepted by series

# 1. Array
# 2. Dict
# 3. scalar or constant


# Create an Empty Series :

# s = pandas.Series()
# print(s)


# Create a Series from ndarray

# data = np.array(['a', 'b', 'c', 'd', 'e'])

# print(data)

# s = pd.Series(data)
# print(s)


#  provide user defined index values

# data = np.array(['a', 'b', 'c', 'd', 'e'])

# print(data)

# s = pd.Series(data, index=[100, 101, 102, 103, 104])
# print(s)
# print(s[100])


#  storing series data from dictionary


# data = {'1': 'amar', 2: 'Raj', '3': "hello"}

# s = pd.Series(data)
# print(s)

# arranging as per our choice


# data = {'1': 'amar', 2: 'Raj', '3': "hello"}

# s = pd.Series(data, index=['3', '1', 2, '2'])
# print(s)


#  Create a Series from Scalar :

# s = pd.Series(10)
# print(s)

# s = pd.Series(10, index=[1, 2, 3, 4, 5, 6, 7, 8])
# print(s)

# s = pd.Series([1, 50, 84, 96, 56, 36, 47, 85],
#               index=[1, 2, 3, 4, 5, 6, 7, 8])
# print(s)


# Accessing dta using Positions

s = pd.Series([1, 50, 84, 96, 56, 36, 47, 85],
              index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i'])

# print(s)

# print(s['i'])

# print(s[-3:])

# print(s['e'])

# print(s['a', 'b', 'i'])


# list=['1','2','3']
# map()
