# Python Project 2018


##  Table_of_Contents
<img align="right" src="Sepetal.jpg" width="200" height="200">

- [Introduction](#introduction)
- [Data Analysis Process](#data_analysis_process)
- [Place holder](#placeholder)
- [Exploration of Data](#exploration_of_data)
- [Analysis](#analysis)
- [Initial Coding Attempt](#initial_coding_attempt)
- [References](#references)

---

## Introduction
- The [Iris flower data set](./iris.csv) or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist [Ronald Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher) in his 1936 paper *The use of multiple measurements in taxonomic problems* as an example of [linear discriminant analysis](https://en.wikipedia.org/wiki/Linear_discriminant_analysis). It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus"

- The [data set](./iris.csv) consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres. Based on Fisher's linear discriminant model, this data set became a typical test case for many statistical classification techniques in machine learning such as support vector machines. 

<h3 align="center">Iris Versicolor &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp; 
Iris Virginica &nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;  Iris Setosa</h3>

<p align="center">
    
  <img src="iris_versicolor.png" alt="Iris Versicolor" width="200" height="200"  />
  
  <img  src="Iris_virginica.jpg" alt="Iris Virginica" width="200" height="200"  />

  <img  src="Iris_setosa.jpg" alt="Iris Setosa" width="200" height="200"  />
  
  </p>
  
 
  ***
  
## Data_Analysis_Process
* Load dataset

<details>
            <summary>Dataset example with code extract (Click to expand)</summary>

```
url = "iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)
   ```
   <p align="center">
    
  <img  src="Data.PNG" alt="Iris Data" width="300" height="300"  />
  
  </p>
 </details>
 
* Describe Data
    * Examine shape of Data
    * We can see that all of the data is numeric and that the class value on the end is the dependent variable that we want to make predictions about.
    

    
    Describe Data
We can now look at the shape of the data.

We can take a look at the first 60 rows of data by printing the data frame directly.


print(data)
1
print(data)
We can see that all of the data is numeric and that the class value on the end is the dependent variable that we want to make predictions about.

At the end of the data dump we can see the description of the data frame itself as a 768 rows and 9 columns. So now we have idea of the shape of our data.

Next we can get a feeling for the distribution of each attribute by reviewing summary statistics.


print(data.describe())
1
print(data.describe())
This displays a table of detailed distribution information for each of the 9 attributes in our data frame. Specifically: the count, mean, standard deviation, min, max, and 25th, 50th (median), 75th percentiles.

We can review these statistics and start noting interesting facts about our problem. Such as the average number of pregnancies is 3.8, the minimum age is 21 and some people have a body mass index of 0, which is impossible and a sign that some of the attribute values should be marked as missing.
* Perform initial analysis
    * Import [Pandas](https://en.wikipedia.org/wiki/Pandas_(software)) and [NumPy](https://en.wikipedia.org/wiki/NumPy) from Python Data Analysis Library
    * [Pandas](https://en.wikipedia.org/wiki/Pandas_(software)) is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the [Python](https://www.python.org/) programming language.
    * [NumPy](https://en.wikipedia.org/wiki/NumPy) is the fundamental package for scientific computing with Python.
    * Calculate and output Mean, Minimum and Maximum values. The initial calculations were done using straightforward python code. dataset['sepal-length'].max. Replacing .max in this expression with .min and .mean facilitates further calculations.



<details>
            <summary>Line by line method - Code extract and output screenshot (Click to expand)</summary>
    
   ```
  # max column value using Pandas max() method
print("Mamimum Sepal Length: "),(dataset['sepal-length'].max())
print("Mamimum Sepal Width: "),(dataset['sepal-width'].max())
print("Mamimum Petal Length: "),(dataset['petal-length'].max())
print("Mamimum Petal Width: "),(dataset['petal-width'].max())
# minimum column value using Pandas min() method
print("Minimum Sepal Length: "),(dataset['sepal-length'].min())
print("Minimum Sepal Width: "),(dataset['sepal-width'].min())
print("Minimum Petal Length: "),(dataset['petal-length'].min())
print("Minimum Petal Width: "),(dataset['petal-width'].min())
# mean column value using Pandas mean() method
print("Mean Sepal Length: "),(round(dataset['sepal-length'].mean()))
print("Mean Sepal Width: "),(round(dataset['sepal-width'].mean()))
print("Mean Petal Length: "),(round(dataset['petal-length'].mean()))
print("Mean Petal Width: "),(round(dataset['petal-width'].mean()))
 ``` 

 

 * Result of Max, Min and Mean calculations:
  
 <p align="center">
    
  <img  src="MaxMinMean.PNG" alt="MaxMinMean" width="300" height="300"  />
  
  </p>
  
   </details>  
  
  <details>
  <summary>Pandas describe() method - Code extract and output screenshot ! (Click to expand)</summary>
    
    
 * A more efficient Pandas *describe()* method requires a single line of code. 
 * Parameters percentiles[..],include[..] and exclude[..] can be set as required.  
 
    
 ```
 print(dataset.describe(percentiles=[]))
 ```

 <p align="center">
    
  <img  src="Description.PNG" alt="MaxMinMean" width="400" height="300"  />
  
 </p>
 
 </details> 
 
 ***
  
## Placeholder
    * Use Scatter Plot, Whisker Plot and Histogram graphs to represent Iris data
    
 ***
    
## Analysis
    * Compare groups of data
    * Explore relationship between variables
    
***
 
## Initial_Coding_Attempt
- Using Numpy, I calculated mean value of first three columns with np.mean(data). Python file [MeanofCols.py](./MeanofCols.py)

<details>
  <summary>Pandas describe() method - Code extract and output screenshot ! (Click to expand)</summary>

```
data = pd.read_csv('iris.csv', header = None)
print (data)
#use comma to separate data intl columns
data = np.genfromtxt('iris.csv', delimiter = ",")
print (data[:,0:3])
#load data from first column into firstcol
firstcol = data[:,0]
secondcol = data[:,1]
thirdcol = data[:,2]
#calcuate mean of columns
meanfirstcol = np.mean(data[:,0])
print ("Mean value of first col is:", meanfirstcol)

meansecondcol = np.mean(data[:,1])
print ("Mean value of second col is:", meansecondcol)

meanthirdcol = np.mean(data[:,2])
print ("Mean value of third col is:", meanthirdcol)
```
</details>

***
## Exploration_of_Data

>this mght be useful
>>ver useful
>>>very useful indeed!!!

Table Header-1 | Table Header-2 | Table Header-3
:--- | :---: | ---:
Table Data-1 | Table Data-2 | Table Data-3
TD-4 | Td-5 | TD-6
Table Data-7 | Table Data-8 | Table Data-9

<br/>
<div align="right">
    <b><a href="#table_of_contents">↥ back to top</a></b>
</div>
<br/>

***

## References
* Initial research on Iris Flower Data Set on Wikipedia https://en.wikipedia.org/wiki/Iris_flower_data_set. 


