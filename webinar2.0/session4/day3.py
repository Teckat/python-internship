import pandas as pd

# column section in data frames

# data = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two': pd.Series(
#     [4, 5, 6, 7], index=['a', 'b', 'c', 'd'])}

# df = pd.DataFrame(data)
# print(df['two'])

#  column addition


# data = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two': pd.Series(
#     [4, 5, 6, 7], index=['a', 'b', 'c', 'd'])}

# df = pd.DataFrame(data)

# print(df)

# print("adding a column")

# df['three'] = pd.Series([10, 11, 12, 13], index=['a', 'b', 'c', 'd'])

# print(df)


#  Column Deletion

# data = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two': pd.Series(
#     [4, 5, 6, 7], index=['a', 'b', 'c', 'd'])}

# df = pd.DataFrame(data)

# print(df)

# print("adding a column")

# df['three'] = pd.Series([10, 11, 12, 13], index=['a', 'b', 'c', 'd'])

# print(df)


# #  delete a column using del function
# print("delete using del")

# del df['two']

# print(df)


# #  delete a column using pop function

# print("\n delete using pop")
# df.pop('three')
# print(df)


# Row Selection


# data = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two': pd.Series(
#     [4, 5, 6, 7], index=['a', 'b', 'c', 'd'])}

# df = pd.DataFrame(data)

# print(df.loc['b'])

# using integer value location


# data = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c'], dtype=int), 'two': pd.Series(
#     [4, 5, 6, 7], index=['a', 'b', 'c', 'd'], dtype=int)}

# df = pd.DataFrame(data)

# print(df.iloc[2])

# slicing of rows


# data = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c'], dtype=int), 'two': pd.Series(
#     [4, 5, 6, 7], index=['a', 'b', 'c', 'd'], dtype=int)}

# df = pd.DataFrame(data)

# print(df[2:4])


#  Addition of rows


data = [[1, 2, 3, 4], [5, 6, 7, 8]]

df = pd.DataFrame(data, columns=['a', 'b', 'c', 'd'])

print("df ")
print(df)
data1 = [[12, 57, 85, 96], [45, 85, 63, 95]]

df2 = pd.DataFrame(data1, columns=['a', 'b', 'c', 'd'])

print("\ndf2")
print(df2)

df3 = df.append(df2)
print("after appending")
print(df3)

# delete the row

df3 = df3.drop(0)

print("row dropped")

print(df3)
