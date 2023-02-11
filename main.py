import pandas as pd
import matplotlib.pyplot as plt

# Read the csv file
df = pd.read_csv('planettData.csv')

# List of columns
columns = ['Name', 'Mass', 'Radius', 'Distance', 'Gravity']

# Bar plot for each feature
for column in columns:
    plt.bar(df['Name'], df[column])
    plt.xlabel('Name')
    plt.ylabel(column)
    plt.xticks(rotation=90)
    plt.show()
