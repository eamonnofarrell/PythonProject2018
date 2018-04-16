# Python Project 2018


##  Table of Contents

- [Introduction](#introduction)
- [Data Analysis Process](#data_analysis_process)
- [Calculate Mean Values](#calculate_mean_values)
- [Week2](#week2)
- [Week3](#week3)
- [Week4](#week4)
- [Week5](#week5)
- [Week6](#week6)

---

## Introduction
- The [Iris flower data set](./iris.csv) or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis.[1] It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus"

- The [data set](./iris.csv) consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres. Based on Fisher's linear discriminant model, this data set became a typical test case for many statistical classification techniques in machine learning such as support vector machines. [Iris.csv](./iris.csv)

<h3 align="center">Iris Versicolor &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp; 
Iris Virginica &nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;  Iris Setosa</h3>

<p align="center">
    
  <img src="iris_versicolor.png" alt="Iris Versicolor" width="200" height="200"  />
  
  <img  src="Iris_virginica.jpg" alt="Iris Virginica" width="200" height="200"  />

  <img  src="Iris_setosa.jpg" alt="Iris Setosa" width="200" height="200"  />
  
  </p>
  
  
## Data_Analysis_Process
* Perform initial analysis
    * Sepal length Mean, Range, Minimum and Maximum values
    * Sepal width Mean, Range, Minimum and Maximum values
    * Petal length Mean, Range, Minimum and Maximum values
    * Petal widgth Mean, Range, Minimum and Maximum values
    
* Exploration of Data
    * Imort Pandas and Numpy from Python Data Analysis Library
    * Use Scatter Plot, Whisker Plot and Histogram graphs to represent Iris data
    
* Analysis
    * Compare groups of data
    * Explore relationship between variables
 
## Calculate_Mean_Values
- Using Numpy, I calculated mean value of first three columns as an exercise. Python file [MeanofCols.py](./MeanofCols.py)
```
import pandas as pd
import numpy as np

#data = pd.read_csv('iris.csv', header = None)
#print (data)

data = np.genfromtxt('iris.csv', delimiter = ",")
print (data[:,0:3])
firstcol = data[:,0]
secondcol = data[:,1]
thirdcol = data[:,2]
meanfirstcol = np.mean(data[:,0])
print ("Mean value of first col is:", meanfirstcol)

meansecondcol = np.mean(data[:,1])
print ("Mean value of second col is:", meansecondcol)

meanthirdcol = np.mean(data[:,2])
print ("Mean value of third col is:", meanthirdcol)
```

