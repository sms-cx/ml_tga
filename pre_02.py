import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


a1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
a2 = np.array([[2, 3, 4, 5], [6, 7, 8, 9]])
l1 = [1, 2, 3, 4]

# convert list to array
a3 = np.array(l1)
print(a3)
print("--------------\n")

# merge two arrays
a4 = np.concatenate((a1, a2), axis=0)
print(a4)
print("--------------\n")

# reshape an array
a5 = a4.reshape(2, 8)
print(a5)
print("--------------\n")

# read cvs file
a6 = pd.read_csv("../02_ressources/ueb_02/datasets_2319_3917_ENB2012_data_Task_1.csv")
print(a6)
print("--------------\n")

# creating a dataframe
df1 = pd.DataFrame(a6)

# finding empty values
print(df1.isnull().sum())
print("--------------\n")

# remove empty values
df1.dropna(inplace=True)

# describe data
print(df1.describe())
print("--------------\n")

# operate on data (????)

# create scatter plot from df1
plt.scatter(df1['X1'], df1['Y1'])


# create a subplot
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
plt.show()
