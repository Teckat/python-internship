# Data Frame

import pandas as pd

# pandas.DataFrame(data,index,column,dtype,copy)

#  type of data

# 1. list
# 2. dict
# 3. Series
# 4. ndArray
# 5. Another DataFrame

#  Creating an empty dataFrame

# df=pd.DataFrame()

# print(df)

# 1. List

# example 1:

# data=[1,2,3,45,6]

# df = pd.DataFrame(data)
# print(df)

# example 2:

# data = [[1, 2, 3, 45, 6], [10, 12, 13, 14, 15], [73, 188, 1, 313, 1938]]

# df = pd.DataFrame(data)
# print(df)


# example 3:

# data = [[1, 2, 3, 45, 6], [10, 12, 13, 14, 15, 17],
#         [73, 188, 1, 313, 1938, 192, 133]]

# df = pd.DataFrame(data)
# print(df)


# example 4:

# data = [[1, 2, 3, 45, 6], [10, 12, 13, 14, 12],
#         [73, 188, 1, 313, 1938]]

# df = pd.DataFrame(data, columns=['age', 'number', 'a', 'b', 'c'])
# print(df)

# example 5:

# data = [[1, 2, 3, 45, 6], [10, 12, 13, 14, 12],
#         [73, 188, 1, 313, 1938]]

# df = pd.DataFrame(data, index=['r1', 'r2', 'r3'], columns=[
#                   'age', 'number', 'a', 'b', 'c'], dtype=float)
# print(df)


# 2. Dict

# # example 1

# data = {'name': ['amar', 'teckat', 'anthony'], 'Age': [24, 1, 34]}

# df = pd.DataFrame(data)
# print(df)


# example 2

# data = {'name': ['amar', 'teckat', 'anthony'], 'Age': [24, 1, 34]}

# df = pd.DataFrame(data, index=['r1', 'r2', 'r3'])
# print(df)


#  Dataframes from list of dict

# example 1

# data = [{'a': 1, 'b': 2}, {'a': 50}, {'a': 34, 'b': 60, 'c': 54}]

# df = pd.DataFrame(data)

# print(df)

# example 1

# data = [{'a': 1, 'b': 2}, {'a': 50}, {'a': 34, 'b': 60, 'c': 54}]

# df = pd.DataFrame(data, index=['r1', 'r2', 'r3'])

# print(df)


# 3. Series

# example 1

data = {'one': pd.Series([1, 2, 3, 5], index=[2, 3, 1, 5]),
        'two': pd.Series([434, 232, 31, 1313, 323], index=[1, 2, 3, 4, 5])}

df = pd.DataFrame(data)
print(df)
