

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt


arr_1d  = np.array([1,2,3,4])
arr_1d

type(arr_1d)

arr_1d.ndim

arr_1d.size

arr_2d=np.array([[1,2,3,4],[5,6,7,8]])
arr_2d

arr_2d.ndim

arr_2d.size

arr_2d.dtype

## create  once matrix

arr_1d_once=np.ones(10)
arr_1d_once

arr_1d_once.dtype

arr_2d_once=np.ones((3,4))#(row,column)
arr_2d_once

# integer type matrix

np.ones((3,4),dtype=int)

np.ones((3,4),dtype=float)

## zeros matrix

np.zeros((5,4),dtype=int)

np.zeros((5,4),dtype=bool)

np.ones((3,4),dtype=bool)

np.ones((3,4),dtype=str)

np.zeros((5,4),dtype=str)

np.zeros((4,5),dtype=str)

# empty matrix

np.empty((3,3))

# Some important function

## arange() 

np.arange(1,13)

np.arange(1,10)

arr_r=np.arange(1,13,2)

arr_r

## linspace()

np.linspace(1,5,15) # 15 value between 1 to 5

## reshape()

arr1=np.arange(1,13)

## 3d array

arr1.reshape(2,3,2)

arr2=np.arange(1,13).reshape(2,6)

arr2

## multidimential to 1d

## ravel()

arr2.ravel('A')

arr2.flatten(order='K')

## transpose convert row to colomns

### transpose()

arr2.transpose()

# any matrix can be transpose using .T
arr2.T

# Mathematic operation Using Numpy

arr4 = np.arange(1,10).reshape((3,3))
arr4

arr5 = np.arange(11,20).reshape(3,3)
arr5

arr4+arr5

np.add(arr4,arr5)

arr5-arr4

np.subtract(arr5,arr4)

arr5/arr4

np.divide(arr5,arr4)

arr4*arr5

np.multiply(arr4,arr5)

## dot product of matrix

arr4@arr5

np.dot(arr4,arr5)

arr1.max()

## index of maximum element

arr1.argmax()

## max value in row or column

arr4.max(axis=0) #row

arr4.max(axis=1) #column

arr4.min()

arr4.argmin()

arr4.min(axis=0)

arr4.min(axis=1)

## Add the all element of array

np.sum(arr4)

np.sum(arr4,axis=0)

np.sum(arr4,axis=1)

np.mean(arr4)

np.sqrt(arr1)

## standerd daviation of matrix

np.std(arr4)

## exponent value

np.exp(arr4) ## e^arry_element

## Log of matrix element

np.log(arr4) #natural log

np.log10(arr4) # base 10

# Numpy array slicing

mx=np.arange(1,101).reshape((10,10))
mx

mx[0,0]

mx[0,0].ndim

mx[0] ## row

mx[0].ndim

mx[:,0] # column

mx[:,0:1] # column in 2d

mx[:,0:1].ndim

mx[1:4,1:4] # 3X3 matrix

# mx[rows,column]
mx[:,1:3]

mx[:]# whole matrix

mx[:,:] # whole matrix

mx[::] # whole matrix

mx.itemsize # storage size

mx.dtype

# numpy array concat and split

ar1=np.arange(1,17).reshape((4,4))
ar1

ar2=np.arange(17,33).reshape((4,4))
ar2

np.concatenate((ar1,ar2))

np.concatenate((ar1,ar2),axis=0)

np.concatenate((ar1,ar2),axis=1)

# vertically concatenate
np.vstack((ar1,ar2))

# horizontally concatenate
np.hstack((ar1,ar2))

np.hstack((ar1,ar2,ar1)) #more then two array

np.split(ar1,2)

list1=np.split(ar1,2)
type(list1)

list1[0]

type(list1[0])

np.split(ar1,2,axis=0) # rows

np.split(ar1,2,axis=1) #column

d1= np.array([1,6,8,9])
d1

np.split(d1,[1,3,]) #split in 3 array

# Trignometry functions

np.sin(np.pi/4)

np.sin(np.pi/2)
np.pi

np.tan(1000)

np.cos(90)

x_sin =np.arange(0,3*np.pi,0.1)
x_sin

y_sin =np.sin(x_sin)
y_sin

plt.plot(x_sin,y_sin)
plt.show

y_cos=np.cos(x_sin)
y_cos

plt.plot(x_sin,y_cos)
plt.show()

y_tan=np.tan(x_sin)
y_tan


plt.plot(x_sin,y_tan)
plt.show()

# Random sampling in numpy

import random 

np.random.random(1)

np.random.random((3,3)) # 3X3 matrix random value between 0 to 1

np.random.randint(6,11) #single random value between 6 and 11

np.random.randint(6,11,(4,4)) #2d array

np.random.randint(6,11,(2,4,4)) #3d array

np.random.seed(10)
np.random.randint(6,11,(2,4,4))

np.random.seed(10) #generate same randum value
np.random.randint(6,11,(2,4,4))

np.random.rand(3)

np.random.rand(3,3)

np.random.randn(3,3) # negative and positive value

x= [1,2,3,4]
np.random.choice(x)  # choose random value in this list

np.random.permutation(x)

# string operation ,Comparison,information

str1 = "Ziddi engineer."
str2 = " I am data scientiest "

np.char.add(str1,str2)

np.char.lower(str1)

np.char.upper(str2)

np.char.title(str2)

np.char.center(str1,60)

np.char.center(str1,60,fillchar='*')

np.char.split(str2)

np.char.splitlines("Hello \n Indian")

str4 = "dmy"
str5 = "dmy"

np.char.join([':','/'],[str4,str5]) # join by particular charactor

np.char.replace(str1,'Ziddi','Mr. Ram')# replace word

np.char.equal(str4,str5)# compair string

np.char.count(str1,'e') # count of e in str1

np.char.find(str1,'ziddi')#find the index of char

str1