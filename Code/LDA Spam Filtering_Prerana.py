# -*- coding: utf-8 -*-
"""Assignment_2_Prerana_Khatiwada(HW2).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b-A1mlF5VvrDcMfUlMLrPd6_DSe81T18
"""

import numpy as np
import pandas as pd

import numpy as np

import urllib.request
from sklearn.model_selection import train_test_split 
from scipy.stats import multivariate_normal

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.data"

raw_data = urllib.request.urlopen(url)

dataset = pd.read_csv(url)

print(dataset)

x = dataset.iloc[:,0:-1].values
y = dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test= train_test_split(x,y,test_size = 0.30, random_state = 17)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

import matplotlib.pyplot as plt

plt.plot(x_train[y_train==1,0], x_train[y_train==1,1], 'rx')
plt.plot(x_train[y_train==2,0], x_train[y_train==2,1], 'o')

plt.axis("equal")

plt.show()

x_train

x_test

x_train.shape

x_test.shape

y_train.shape

y_test.shape

n=len(y_train)

print(n)

mu1 = np.mean(x_train[y_train==1,:],axis=0) 
mu2 = np.mean(x_train[y_train==0,:],axis=0)

print(mu1)

print(mu2)

Sigma = np.zeros((57,57))

for i in range(n):
  if y_train[i]==1:
    Sigma+= np.outer((x_train[i,:]-mu1),x_train[i,:]-mu1)/n
  else :
    Sigma+= np.outer((x_train[i,:]-mu2),x_train[i,:]-mu2)/n

q1 = sum(y_train==(1))/n
q2 = sum(y_train==(0))/n

print(q1,q2)

g1 = multivariate_normal(mu1, Sigma)
g2 = multivariate_normal(mu2, Sigma)

print(g1,g2)

n2=len(x_test)

print(n2)

Test_Output=np.zeros(n2)

for a in range(n2):
 if g1.pdf(x_test[a])*q1 > g2.pdf(x_test[a])*q2:
  Test_Output[a]= 1
 else:
  Test_Output[a]= 0

n2 = len(x_test)
#print ("\nLength of x-test", n2)
predict=0
notpredict=0

for i in range(n2):
  if Test_Output[i]==1 and  y_test[i]==1: 
    predict=predict+1

for i in range(n2):
  if Test_Output[i]==0 and  y_test[i]==0: 
    predict=predict+1

notpredict=n2-predict
print ("Test accuracy", predict/n2)
Test_error=notpredict/n2
print("Test_error", Test_error)