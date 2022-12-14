# -*- coding: utf-8 -*-
"""hw6 prob1_702616768.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l6NKqy-yWYl6Qyh1ALM9PaKt3YK6iqXg
"""

import scipy.io
import numpy as np
from matplotlib import pyplot as plt
import numpy as np
data = scipy.io.loadmat('yalefaces.mat')
data = data['yalefaces']
print(data.shape)
index = 10
plt.imshow(data[:,:,index])

data_transform_resize=data.copy()
data_transform_resize=data_transform_resize.reshape(2016, 2414)
print(data_transform_resize.shape)

mean = np.mean(data_transform_resize)
std=np.std(data_transform_resize)
mean_data=data_transform_resize-mean

# Compute covariance matrix
dataset2 = (mean_data)/std
cov = np.dot(dataset2, dataset2.T)
print("Covariance matrix ", cov.shape, "\n")
eig_val, eig_vec = np.linalg.eig(cov)

# Sort eigen values and corresponding eigen vectors in descending order
posn = np.arange(0,len(eig_val), 1)
posn = ([x for _,x in sorted(zip(eig_val, posn))])[::-1]
eig_val = eig_val[posn]
eig_vec = eig_vec[:,posn]
print(eig_vec.shape)
print(eig_val)
print(eig_val.shape)


# Get explained variance
sum_eig_val = np.sum(eig_val)
explained_variance = eig_val/ sum_eig_val
cumulative_variance = np.cumsum(explained_variance)

numbers_of_lambda=1
for a in range (1000):
  sum1=0
  for j in range(numbers_of_lambda):
    sum1=eig_val[j]+sum1

  ratio=sum1/sum_eig_val
  if ratio>=0.95:
    print(ratio,numbers_of_lambda)
    break
  else:
    numbers_of_lambda=numbers_of_lambda+1

numbers_of_lambda=1
for a in range (1000):
  sum2=0
  for j in range(numbers_of_lambda):
    sum2=eig_val[j]+sum2
  proportion=sum2/sum_eig_val
  if ratio>=0.99:
    print(ratio,numbers_of_lambda)
    break
  else:
    numbers_of_lambda=numbers_of_lambda+1

# Plot explained variance
plt.plot(np.arange(0, len(explained_variance), 1), cumulative_variance)
plt.title("Explained variance vs number of components")
plt.xlabel("Number of components")
plt.ylabel("Explained variance")
plt.show()

## We will 41 components
n_components = 41
eig_vec = eig_vec[:,:n_components]
print(eig_vec.shape)

print(1-n_components/2016,"Reduction Percentage for first case")

# Plot explained variance
plt.plot(np.arange(0, len(explained_variance), 1), cumulative_variance)
plt.title("Explained variance vs number of components")
plt.xlabel("Number of components")
plt.ylabel("Explained variance")
plt.show()

## We will 161 components
n_components2 = 161
eig_vec = eig_vec[:,:n_components2]
print(eig_vec.shape)

print(1-n_components2/2016,"Reduction Percentage for second case")

for s in range(20):
  plt.imshow(eig_vec[:,s].reshape(48,42))
  plt.figure(s+1)

# Take transpose of eigen vectors with data
pca_data = np.dot(mean_data.T,eig_vec)
print("Transformed data ", pca_data.shape)

# Reverse PCA transformation
recon_data = pca_data.dot(eig_vec.T) + mean
print(recon_data.shape)

loss = np.mean(np.square(recon_data.T - data_transform_resize))
print("Reduction ", loss)