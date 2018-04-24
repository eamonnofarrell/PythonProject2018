#Eamonn O'Farrell
import numpy
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

# Load dataset
url = "iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

# shape
print(dataset.shape)

# head
print(dataset.head(20))

# descriptions
print(dataset.describe())

# class distribution
print(dataset.groupby('class').size())

# Boxplot1 Use Pandas .boxplot() to calculate and show box and whisker plots
dataset.boxplot()
plt.show()

# Boxplot2 - use .boxset() to generate box plot howing varying 
# sepal lengths per flower type
dataset.boxplot(column="sepal-length",by="class")
 plt.show()


# Use Pandas histograms .hist() to plot histogram of Iris Data Set
dataset.hist()
plt.show()


# scatter plot matrix
scatter_matrix(dataset)
plt.show()

