#Eamonn O'Farrell - GMIT Python Project April 2018
import numpy
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt


# Load dataset
url = "iris.csv"
# assign column names
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
IrisData = pandas.read_csv(url, names=names)

# shape specifies the amount of rows and columns
print(IrisData.shape)

# head prints out data in IrisData
print(IrisData.head(150))

# pandas describe() calculates min, max, mean, etc 
print(IrisData.describe())

# print amount of instances per class (flower type)
print(IrisData.groupby('class').size())

# Boxplot1 Use Pandas .boxplot() to calculate and show generic box and whisker plot
IrisData.boxplot()
plt.show()

# Boxplot2 - use .boxset() to generate box plot showing varying 
# sepal lengths per flower type
IrisData.boxplot(column="sepal-length",by="class")
plt.show()


# Use Pandas histograms .hist() to plot standard histogram of Iris Data Set
IrisData.hist()
plt.show()

# Use .hist() to filter sepal-length column and plot histogram 
IrisData.hist(column='sepal-length')
plt.show()

# scatter plot matrix with data from csv file
scatter_matrix(IrisData)
plt.show()


