# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:52:41 2020

@author: HASSAN ENTERPRISES
"""


# numpy stands for "numerical python"
# Fundamental python pakage for scientific computing
# solve mathematical problems

# numeric: Jim Hugunin and other contributors
# numpy : Travis Oliphant + Other
# Arrays 
# Linear Algebra
# Random Number Generation
# Broadcasting
#Arrays multidimensioal Array
#Arrays are similar to list but different to arrays 

#Numpy are use to data storage just like json module 
#similar between list and numpy
# storing_Data, Mutable,can be indexed
#Slicing operations

#different between list and Numpy arrays
#list contains differents data types  example [1,3,"huzaifa",3.4,3,"saad"]
# Arrays contains similar data types example  [1,4,5,6,8,7,5,2]
# Difference between operations
#----------------------------------------------------------------------------------------------------------------
#one dimension arrays
import numpy 
a=numpy.array([1,4,6,87,2,6])
print(a)
a/3
#but if we try on list:
list =[1,2,3,4,5,6,7,8]
print(list/3)
#-----------------------------------------------------------------------------------------------------------------
#second difference list is builtin 
#for numpy we need to install numpy_array
#Advantages our the list 
#Array contain less memory
# Arrays are fast as compare to list
#------------------------------------------------------------------------------------------------------------------
#Numpy Arrays
#Arrays introduction
#Arrays means display or arrange things in a particular ways
#or we say "collection of elements of same type"

# arrays is module of python arrays
# using numpy librarys [Numpy Arrays]
# Numpy arrays is generally called endarray in python documentation
#creating numpy arrays
#functions in arrays
#Arrays(),Arange(),Zeros(),Ones(),Linspace(),Eye(),Random()

#"Creating Arrays from list or tuples"
#syntax of arrays functions

import numpy as np
help(np.array)
#arrays(objects,dtype=None,copy=True,order="k",sobok=False,ndmin=0)
# 2 dimension arrays 
#Example [[2,3],[4,5]]      [] ineer list in two dimension arrays is called row and [] outer list in two dimension 
# arrays is called cols
#-----------------------------------------------------------------------------------------------------------------
print(np.array([[2,3],[4,5,6,7]]))
np.array([[2,3],[4,5,6,7]])
# upcasting data type
a=np.array([1,2,3,4,5.000])
print(a) 
#-----------------------------------------------------------------------------------------------------------------
#minimum dimension 3
a=np.array([1,2,3],ndmin=3)
print(a)
#------------------------------------------------------------------------------------------------------------------
a=np.array([1,2,3],dtype="complex")
print(a)
#-----------------------------------------------------------------------------------------------------------------
a=np.array((1,2,3))
print(a)# so our output will be in list we gave a tuple
#-----------------------------------------------------------------------------------------------------------------
#Arange() functions:
#Arange function create Arrays of evenly spaced values
import numpy as np
help(np.arange) 
#----------------------------------------------------------------------------------------------------------------
import numpy as np
np.arange(6)
np.arange(5.0)
np.arange(3,7,1)
np.arange(3,7,1.5)
np.arange(3,10)
np.arange(20,dtype="complex") 
np.arange(1,10,2,dtype="float")
#----------------------------------------------------------------------------------------------------------------
import numpy as np
help(np.zeros)
# zeros(shape,dtype=float,order=c)
a=np.zeros(5)
print(a)
#---------------------------------------------------------------------------------------------------------------
z=np.zeros((5),dtype=int)
print(z)
#---------------------------------------------------------------------------------------------------------------
a=np.zeros((2,1),dtype=int) # two rows and one column 
print(a)
#----------------------------------------------------------------------------------------------------------------
y=(2,2)
a=np.zeros(y,dtype=int)
print(a)
#---------------------------------------------------------------------------------------------------------------
import numpy as np
np.zeros((3,2))
#----------------------------------------------------------------------------------------------------------------
x=np.zeros([5,7])
print(x)
#---------------------------------------------------------------------------------------------------------------
c=np.zeros(5,order="C")
print(c)
#----------------------------------------------------------------------------------------------------------------
r=np.zeros([5,7],order="F")
print(r)
#---------------------------------------------------------------------------------------------------------------
import numpy as np
help(np.ones)
#---------------------------------------------------------------------------------------------------------------
a=np.ones(5)
print(a)
#----------------------------------------------------------------------------------------------------------------
z=np.ones((5),dtype=int)
print(z)
#----------------------------------------------------------------------------------------------------------------
a=np.ones((2,1),dtype=int) # two rows and one column 
print(a)
#---------------------------------------------------------------------------------------------------------------
y=(2,2)
a=np.ones(y,dtype=int)
print(a)
np.ones((3,2))
#--------------------------------------------------------------------------------------------------------------
c=np.ones(5,order="C")
print(c)
#--------------------------------------------------------------------------------------------------------------
r=np.ones([5,7],order="F")
print(r)
#----------------------------------------------------------------------------------------------------------------
# empty also use to create unintilize entries.. uninitializing value or to create random values
#empty (shape, dtype="float" by default,order="C")
import numpy as np
v=np.empty([2,3])
print(v)
#-----------------------------------------------------------------------------------------------------------------
u=np.empty([5,6,7],dtype="int")
print(u)
#---------------------------------------------------------------------------------------------------------------
#linspace stands for linear_space
import numpy as np
help(np.linspace)
#---------------------------------------------------------------------------------------------------------------
v=np.linspace(2,3,num=6)
print(v)
#---------------------------------------------------------------------------------------------------------------
v=np.linspace(2,3,num=6,endpoint=False) #endpoint false likhnay say humay num to 6 hii milayga but end value nh milaygiii
print(v)
v=np.linspace(2,3,num=6,endpoint=True)
print(v)
#---------------------------------------------------------------------------------------------------------------
v=np.linspace(2,3,num=6,endpoint=False,retstep=True)
print(v) #retstep show us how many stepsize between number
#---------------------------------------------------------------------------------------------------------------
import numpy as np
help(np.random)

# rand ,randn,randf,randint
# rand uniformly distributed values
# randn normly distributed values
# randf uniformly distributed values of float 
# randint uniformly distributed values of integers
help(np.random.rand)
# creating random numbers  
c=np.random.rand(5,6)
print(c)
c=np.random.rand(6)
print(c)

#---------------------------------------------------------------------------------------------------------------
help(np.random.randn)
c=np.random.randn(5)
print(c)
#---------------------------------------------------------------------------------------------------------------
#c=np.random.randf(5,6)
#print(c)
c=np.random.randint(5,6)
print(c)
#-------------------------------------------------------------------------------------------------------------
c=np.random.randint(5,size=6) #generate one dimension arrays less than 5 values
print(c)
#--------------------------------------------------------------------------------------------------------------------------
v=np.random.randint(4,size=(3,5))
print(v)
#---------------------------------------------------------------------------------------------------------------
#------------------------------------ Attributes of Arrays                                  -------------------------------
#Dimension we can made n dimension of arrays
#ndim stands for n dimension array
import numpy as np
a=np.array([1,2,3,4,5,6,7])
a.ndim
#---------------------------------------------------------------------------------------------------------------
z=np.array([[1,2],[3,4]])
z.ndim
# Shape :
import numpy as np
a=np.zeros(6)
print(a)
a.ndim
a.shape

#-----------------------------------------------------------------------------------------------------------------------------------
a=np.array([[1,2,3],[3,4,5]])
a.shape
a.size
a.dtype
#------------------------------------------------------------------------------------------------------------------------
c=np.zeros((2,3,4))
c.shape
#------------------------------------------------------------------------------------------------------------------
#attribute Size
#total number of elements in arrays
c=np.zeros((2,3,4))
c.size
#---------------------------------------------------------------------------------------------------------------
#Attributes of array 0ne is dtype
c=np.zeros((2,3,4))
c.dtype
#--------------------------------------------------------------------------------------------------------------
#attribute of itemsize
#1byte =8bits
#item size is nothing but it is the size of each elements in arrays in bits 
#float64 bytes =64/8=8bits
#float 32 bytes =32/8 bits
c=np.zeros((2,3,4))
c.itemsize
#---------------------------- data tyes in arrays ------------------------------------------------------------
#numerical data type
# booleans, Float,integers,unsigned Integers,complex
import numpy as np
a=np.zeros(5)
a.dtype
# int=np.int,float=np.float,complex=np.complex
b=np.zeros(6,dtype=np.int8)
b
#---------------------------- More data types ------------------------------------------------------------------
import numpy as np
x=np.float64(2)
x # we can use datatype as function to convert data btype as numbver 
x.dtype
#2 datatype can be refered as character code
a=np.array([1,2,3,4,5,6,6],dtype="f")
a
a=np.array([1,2,3,4,5,6,6],dtype="c")
a
a=np.array([1,2,3,4,5,6,6],dtype="int")
a
#---------------------------------------------------------------------------------------------------------------
# characters dof code of datatypes in numpy
#"b" (signed)bytes
#"B" unsigned bytes
#"i" (signed)integers
#"u" unsigned imtegers
#"f" floating_point
#"c" complex-Floating_point
#"m" timedelta
#"M" datatime
#"O" (python) objects
#"S","a" zero terminated bytes(not recommended)
#"U" unicodes string
#"V" raw data(void)
import numpy as np
a=np.zeros(5)
a
# if i want to change it dtype so i use  1methods
a.astype(int)
np.int64(a) # 2 methods
#---------------------------------------------------------------------------------------------------------------
# -------------------------- indexing in numpy -----------------------------------------------------------------
# similar as list 
# 1 can retrieve single value of array
# 2 zero based indexing
# 3 negative indexing
import numpy as np
a=np.array([1,2,3,4,5,6,7])
a[2]
# 1 dimensional arrayy
#-------------------------------------------------------------------------------------------------------
import numpy as np
#2 dimensional arrays 
b=np.array([[1,2],[3,4]])
b[0][1]
#-------------------------------------------------------------------------------------------------------
import numpy as np
# 3 dimensial arrays 

b=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]])
b
print(b[0][0][1])
print(b[-2][-3][-3])
print(b[1][0][3])
print(b[1][2][3])
print(b[0],b[1])
#---------------------------------- slicing in numpy -----------------------------------------------------
#slicing operation in one dimension arrays
#similar as list slicing 
#one dimension arrays 
a=np.array([1,2,3,4,5,6])
a[2:6]
a[:]
a[1::2]
a[:3]
a[2:5]
# slicing of two dimensial arrays
a=np.array([[1,2],[2,3]])
a[0:,1:]
a[1:,1:]
#------------------ advanced indexing in numpy------------------------------------------------------------------
# Advanced Indexing
# can access elements of an arrays arbitrarily permitting items to be accessed out of order and even repeatedly
#basic indexing and slicing 
import numpy as np
x=np.array([1,2,3,3,5])
x[3]
x[3:]
# Advanced indexing will return copy of the data 
#type of advanced indexing one is intergers indexing
#second type boolean indexing
# difference between
# ---------------------------- this is integers indexing ----------------------------------------------------- 
#example in one dimension arrays
import numpy as np
a=np.arange(1,10) # arange similar as range function
a
#---------------------------------------------------------------------------------------------------------------
index=np.array([0,5,3])# here i will write index of a
print(a[index])
print(a[[0,5,3]])
# 1 create arrays of index of required elements

#-----------------------------------------------------------------------------------------------------------------
#example of 2 dimension array for advanced indexing
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
a# if i want to excess 3,7 in two dimensial array
#so i will use a#[row][column]
print(a[[0,2],[2,0]])
#----------------------------------------------------------------------------------------------------------------
# if i want to excess 4 and 6
print(a[[1,1],[0,2]]) 
# i advance indexing we can get repeated indexing also
import numpy as np
a=np.arange(1,10)
# [i am writing an index  which i want to get the value repeatedly ]
a[[1,4,1,5,1,5,4,5]]

#------------------------------- boolean indexing ---------------------------------------------------------------
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
a
print(a[a>2])
print(a[a<3]*2)
# indexing array is used for filtering the array for specificed the elements
#---------------------------------------------------------------------------------------------------------------

#------------------------- Arithmetic operation on numpy arrays -------------------------------------------------------------
# one is scalars
# between arrays
 #first we would talk scalars arrays
 # for one dimension arrays
import numpy as np
a=np.arange(1,7)
print(a)
print(a**3)
print(a*3)
print(a+3)
print(a/3)
# for two dimensions arrays
import numpy as np
z=np.array([[1,2],[3,4]])
print(z)  
print(z+4)
#-------------------------------------------  adding arrays --------------------------------------------------
# one dimension arrays
import numpy as np
b=np.array([1,2,3,4,4,5])
x=np.array([3,4,5,6,7,8])
print(b+x)
#--------------------------------------------------------------------------------------------------------------
#-----------------------arithmetics operations on two dimensions arrays-----------------------------------------
b=np.array([[1,2,3],[4,5,6]])
a=np.array([[7,8,9],[10,11,12]])
print(b+a)
# another way to write
print(np.add(b,a))
print(np.subtract(b,a))
print(np.multiply(b,a))
print(np.divide(b,a))

#--------------------------   Broadcasting ---------------------------------------------------------------------
# armathematics operation of diferent shape of arrays
#broadcasting in numpy is used or allowed us to anything for differents shape and size of arrays
#perform arthematics operations of differets size
# it is done in copy.............................................................................................
#----------------------- Arrays manipulation reshape and resize ------------------------------------------------
#Reshaping Array,Array Flattering,Dimensions Shuffling,JoiningArrays,Spliting Arrays,Add | Remove elements to arrays
#---------------- Reshaping or array by reshape function -------------------------------------------------------
#parameters of reshape( arrays_name,shape,order)
#order should be ["C"or "F"or"A"]
#"C" is nothing but row wiseopertion
#"F" is nothing but column wise operation
import numpy as np
a=np.arange(10)
print(a)
print(a.shape)
b=np.reshape(a,(5,2))
print(b)
b.shape
c=np.reshape(a,(5,2),"F")
print(c)
#d=np.reshape(a,(4,3),"C")
#print(d)
a=np.arange(10)
a.reshape((2,5))
print(a)
#------------------------------------------   another way to resize -------------------------------------------
#reshape doesnot change the data of array
# But resize should change the data of arraay
#numpy.resize(Array_name,shape)
a=np.arange(10)
print(a)
np.resize(a,(2,3))
#----------------------------------------------------------------------------------------------------------------
a=np.arange(5)
print(a)
np.resize(a,(2,3))
#resize is total number of elements of arrays
#reshape change the shape or it dimension of array
np.resize(a,(5,2))
#-----------------------------------------------------------------------------------------------------------------
#-------------------------   flatten and ravel ------------------------------------------------------------------
# the flattern will return copy of the array in one dimension
# here we will discuss two type of method flattern and ravel method
#we will convert 2d array or 3d array into one d array 
#ndarray.flattern(order={"C","F","A"})
import numpy as np
b=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
b
print(b.flatten())
# flatten make it 3d array into one d array
print(b.flatten(order="F"))
print(b.flatten(order="A"))
print(b.flatten(order="C"))
#----------------------------------------------------------------------------------------------------------
#by default it is ordxer="C"
import numpy as np
b=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
b
print(np.ravel(b))
b.ravel(order="F")
# difference between flatten amd ravel 
#flatten give copy of the array 
#ravel give view of the array and it is a library based method
#flatten is function which will return a copy of the array
#---------------------------------------------------------------------------------------------------------------
#----------------------------  transpose and swapaxes ----------------------------------------------------------
#transpose function
#swapaxces function
# syntax numpy.transpose(array,axes=None)
import numpy as np
b=np.arange(1,11).reshape(5,2)
b
np.transpose(b)
#-------------------------------------------------------------------------------------------------------------
#3 d array
z=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]]).reshape(2,3,4)
z
np.transpose(z).shape

#--------------------------------------------------------------------------------------------------------------
#1 d array
import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10])
print(a.transpose())
print(a.T)
np.transpose(a)

import numpy as np
q=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
q
print(np.transpose(q,axes=(1,0)))
print(np.transpose(q,axes=(0,1)))
#------------------------------------------------------------------------------------------------------------
#---------------------------------    swapaxes functions ----------------------------------------------------
#you can interchange any two axis of given array
#syntax numpy.swapaxes(array_name,axis1,axis2)
import numpy as np
q=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
q
print(np.swapaxes(q,1,0))
print(np.swapaxes(q,0,1))
#-------------------------------------------------------------------------------------------------------------
a=np.array([[1,2,3,4,5,6,7,8,9,10]])
np.swapaxes(a,0,1)

#-------------------------------------------------------------------------------------------------------------\
a=np.arange(1,25).reshape(2,3,4)
a
print(np.swapaxes(a,1,2).shape)
print(np.swapaxes(a,1,1).shape)
print(np.swapaxes(a,0,1))
#-------- difference between transpose and swapaxes-------------------------------------------------------
#In transpose we can change all the dimension but in swapaxes we only change two dimensions
#---------------------------------------------------------------------------------------------------------
#--------------------- joining and splitting numpy array --------------------------------------------------
#concenatate ()  this function is used to joining two arrays
#syntax=numpy.concenatate(array,axis,out) for joining of the array remember that dimension of the array shoiuld be same 
#if i will pass a parameter out so it will store the value of that array in other array which i will pass
# 1 d array
import numpy as np
a=np.arange(1,5)
b=np.arange(6)
np.concatenate((a,b))
c=np.arange(7)
np.concatenate((a,b,c))
#------------------------------------------------------------------------------------------------------------
d=np.zeros(17)
np.concatenate((a,b,c),out=d)
# for 2 d arrays
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[10,11,12]])
np.concatenate((a,b,c))
#c=np.array([[13,14,15]])
#-----------------------------------------------------------------------------------------------------------
#numpy libraray provide us to concatenate two functions 
#vstack(),hstack()
# vstack combine the array vertically
#hstack combine the array horizontally
import numpy as np
a=np.arange(7)
b=np.arange(7)
c=np.arange(7)
np.vstack((a,b,c)) # all dimension should be same a,b,c alll are one dimension
#----------------------------------------------------------------------------------------------------------
a=np.array([[1,2],[3,4]])
b=np.array([[5,6]])
np.concatenate((a,b))
#--------------------------------------------------------------------------------------------------------
#----------------------- split function  must be break multiple array ------------------------------------
# syntax=numpy.split(array_name,section,axis)
a=np.arange(1,10)
np.split(a,3)
#np.split(a,2)
# be carefull about sections 
# there are two type of split hsplit ,vsplit
#hsplit syntax()
#vsplit syntax()
#---------------------------------------------------------------------------------------------------------
#---------------------------------  insert or delete numpy arrays -----------------------------------------
#insert function
# delete 
#syntax=numpy.insert(arrat_name,obj=before index you want to add,value=newvalue you want to add,axis=none)
# 1d array
import numpy as np
a=np.arange(1,11)
a
np.insert(a,2,45)            
# if i would insert a value of float point then what will happen
np.insert(a,2,45.8) #it will convert the float point value intoo integers
np.insert(a,(6,7),50)
# 2 d array
a=np.array([[1,2],[3,4]]) 
np.insert(a,0,5) #first it will flatten the 2 d array then it will return the 1 dimension array
np.insert(a,1,23,axis=0)
np.insert(a,1,23,axis=1)
np.insert(a,1,[1,2],axis=0)
np.insert(a,0,[1,2],axis=1)
#--------------------- append function this will add the value in the array -----------------------------
#syntax=numpy.append(name_array,value,axis)
#this function will return the copy of the array
#help(np.insert)
#help(np.append)
# 1 dimension
import numpy as np
a=np.arange(1,11)
a # append function will insert at the last 
np.append(a,45)            
# 2 dimension
a=np.array([[1,2],[3,4]])
np.append(a,[[5,6]],axis=0)
#np.append(a,[[5,6]],axis=1)
np.append(a,[[5],[6]],axis=1)
#---------------------------------- delete function -----------------------------------------------------
#syntax=numpy.delete(name_array,obj,axis=none)
import numpy as np
a=np.arange(1,11)
a
print(np.delete(a,3)) #copy of the array should be deleted 
print(a)
a=np.array([[1,2],[3,4]])
np.delete(a,2)
np.delete(a,1,axis=0)
np.delete(a,1,axis=1)
#---------------- introduction in matric in python --------------------------------------------------------
# numpy is lib which allow us to create matrics
import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
#a+b
np.add(a,b)
# difference between arraymultiplication and matrics multiplication is 
# array multiply elements by elements 
# example
import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
a*b
np.multiply(a,b)
# but matrics multiply is row multiply by column symbole is dot(.)
#matric multiplication
import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
a.dot(b)
#--------------------------------------------------------------------------------------------------------
#----------------------  creating a matrics by classs matric -------------------------------------------
#matric is a class of numpy libraray
#syntax=numpy.matric(data,dtype=none,copy=true)
import numpy as np
a=np.matrix("1 2 ; 3 4")
a
b=np.matrix([[1,2],[3,4]])
b
a=np.matrix([[1,2],[3,4]])
a
print(a.T)
print(a+b)
print(a*b) #In matrix * is use for row multiply by column

#difference between numpy and matrix
# 1 matrix can be created also by string object
# 2 matrix object are always 2D
# 3  in array we use * staric sign to multiply elements by elements or if we want row multiply by column 
# then we would use dot (.) to multiply row and column but in matrix we would only use * to multiply row and column
#---------------------------------------------------------------------------------------------------------

#-----------------------------   Inverse of matrix-------------------------------------------------------
#using numerical linearalgebra 
#syntax=num.linalg()
# for this we can find out inverse of the matrix ,power of the matrix,determinants of the matrix,
# for inverse we would use inverse function to inverse the matrix
# only square matrix will be inverted
#syntax =numpy.linalg.inv(1parameter that is name_array)
import numpy as np
a=np.array([[1,2],[3,4]])
a
b=np.linalg.inv(a)
b
#-----------------------------------------------------------------------------------------------------
# checking a two matix are inditical A.Ainverse =I
#we should use for this we would use 
np.allclose(np.dot(a,b),np.eye(2)) #here np.eye(2) will create identity matrix of two rows and columns
help(np.linalg.inv)
# 3 d arrray
a=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
b=np.linalg.inv(a)
b
#--------------------------------------------------------------------------------------------------------
#------------------------------------  power of matrix ---------------------------------------------------
# syntax=numpy.linalg.matrix-power(array_name,power=n)
# n=0,n=positive_power  
import numpy as np
a=np.array([[1,2],[3,4]])
a
b=np.linalg.matrix_power(a,3)
b # this is basically a A^2 or we say that A.A
#we can alse done by this also
np.dot(a,a,a)
#-----------------------------------------------------------------------------------------------------------
a=np.array([[1,2],[3,4]])
a
b=np.linalg.matrix_power(a,0)# If i take power is zero then it will return me identity matrix
b # this is basically a A^2 or we say that A.A
# if i would give a power of negative then it will convert it intoo inverse of it and then it will it square 
# of it
c=np.linalg.matrix_power(a,-2)
c
# show how it will work
#first it will convert it into inverse of c matrix
c=np.linalg.inv(a)
c
d=np.linalg.matrix_power(c,2)
d
#---------------------------------------------------------------------------------------------------------
#-------------------------------  Linear equations -------------------------------------------------------
#x+y=10
#2x+2y=20
# the system of linear equation is to find out the values of variables of x,y
# syntax=numpy.linalg.solve() Ax=B  A is matrix X=variables B=constants terms
# 3x+y=9 a=[[3,1],[1,2]] b=[9,8]
# x+2y=8
import numpy as np
a=np.array([[3,1],[1,2]])
b=np.array([9,8])
c=np.linalg.solve(a,b)
c #here 2 and 3 is nothing but x=2. y=3.
#-------------------------------------------------------------------------------------------------------
import numpy as np
# 6x+2y-5z=13
# 3x+3y-2z=13
# 7x+5y-3z=26
a=np.array([[6,2,-5],[3,3,-2],[7,5,-3]])
b=np.array([13,13,26])
c=np.linalg.solve(a,b)
c # here x=2,y=3,z=1

#---------------------------------------------------------------------------------------------------------
#-------------------------- Determinants of matrix -------------------------------------------------------
#syntax=numpy.linalg.det(Array_name)
#2 d array
import numpy as np
a=np.array([[1,2],[3,4]])
b=np.linalg.det(a)
b
round(b) #here round will be round the value
#---------------------------------------------------------------------------------------------------------
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.linalg.det(a)
b
round(b)
#--------------------------------------------------------------------------------------------------------



