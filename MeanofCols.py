
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
