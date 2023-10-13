import csv
import pandas as pd
import matplotlib.pyplot as plt

# df.columns = Index(['sep=', 'Unnamed: 1'], dtype='object')
# Read the .csv file
data = pd.read_csv("pb.csv")

col = data.columns
print(col[2])

# Printing type of arr object
# print("Array is of type: ", type(data))

# # Printing dimensions
# print("Printing number of dimensions: ", data.ndim)

# # Printing shape of array
# print("Printing shape of array: ", data.shape)
