import csv
import pandas as pd
from datetime import datetime
import numpy as py
import matplotlib.pyplot as plt


# df.columns = Index(['sep=', 'Unnamed: 1'], dtype='object')
# Read the .csv file

with open("pickleball.csv", "r") as source:
    reader = csv.reader(source)
    # for line in reader:
    #     print(line[4])

    for line in reader:
        original_date = line[2]

        duration = line[6]
        # print(f"duration: {duration} min")

########################################################
# Printing type of arr object
# print("Array is of type: ", type(data))

# # Printing dimensions
# print("Printing number of dimensions: ", data.ndim)

# # Printing shape of array
# print("Printing shape of array: ", data.shape)
