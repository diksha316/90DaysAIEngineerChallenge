import numpy as np

# 1. Numpy Introduction
print(np.__version__)# To print the current version of numpy
my_list = [1,2,3,4]
# We want to multiply all the numbers of the list with the number 2
my_list = my_list*2
print(my_list)# This will duplicate all the numbers in the list
# Difference between a numpy array and a native python list
array = np.array([1,2,3,4])
array = array*2
print(array)
print(type(array))

# -------------------------------------------------------------------------------------------------------

# 2. Multidimensional Arrays using Numpy
array2 = np.array('A')#Zero dimensional Array (One point)
print(array2.ndim)#To check the dimesnion of an array
# 1-d Array
arr = np.array(['A','B','C','D'])
# 2-d Array
arr1 = np.array([['A','B','C','D'],
                 ['A','B','C','D'],
                 ['A','B','C','D']])
# 3-d Array
arr2 = np.array([[['A','B','C','D'],['A','B','C','D'],['A','B','C','D']],
                 [['A','B','C','D'],['A','B','C','D'],['A','B','C','D']],
                 [['A','B','C','D'],['A','B','C','D'],['A','B','C','D']]])
# Remember the number of elements in each of the list should be same in any form of Array,
# if data is not present then use a placeholder like an underscore or leave a blank whitespace.
print(arr.ndim,arr1.ndim,arr2.ndim)
print(arr2.shape)# No. of Layers, No. of Rows and No. of Columns
# Chain - Indexing
print(arr2[0][0][0])# Used in Lists
#Multidimensional Indexing
print(arr2[0,0,0])# Used for numpy arrays
print(arr2[2,2,3])# Remember -> Layer, Rows, Columns and indexing starts from 0


# -------------------------------------------------------------------------------------------------------

# 2. Creating numpy arrays using the inbuilt functions:
# a) using arange function 
arr3 = np.arange(1,10) #The last value will be skipped here
arr4 = np.arange(1,10,2) #We can include our custom skip, other than the default skip of one
print(arr3,arr4)
# b) Using linspace -> Creates a numpy array between two numbers whoch are evenly spaced, 
#the last number is included
arr5 = np.arange(1,3,5) # (start,stop,step)
print(arr5) # Output - [1]
arr6 = np.linspace(1,2,5,dtype=int) # (start,stop, number of values between them)
print(arr6)# Output - [1 1 1 1 2]
ar = np.linspace(1,2,5)
print(ar) # Output -> [1.   1.25 1.5  1.75 2.  ]
# c) logspace -> Inserts logarithmic numbers between the two values
arr7 = np.logspace(1,3,2)#(starting power to 10, ending power to 10, number of values to be included in the array)
print(arr7)
# d) zeros -> Creates an array full of zeros
arr8 = np.zeros(5)# for 1-D just mention the number of zeros you want
arr9 = np.zeros([2,6])# For multidimensional array -> ([No of Rows, No of Columns] )
print(arr8,"\n",arr9)
# e) ones() -> Same as zeros
# f) full() -> Creates an array full of a particular value
arr10 = np.full(10,2) # (No of Values, The value the array should contain)
print(arr10)
# To create multidimensional array:
arr12 = np.full([2,3],5) # ([rows,columns], value)
print(arr12)
arr11 = np.full([1,2,7,3,5],7.1)# ([no of times,rows,columns,dimension],value array should contain)
print(arr11)
# g) empty() -> Uninitialized array
# To create an array without setting any value.
arr13 = np.empty([2,3])
print(arr13)


# -------------------------------------------------------------------------------------------------------

# 3. Random Numbers
# a) random.rand() -> To print random floats with the specified number of columns and rows
ar1= np.random.rand(2,3)
print(ar1)
# b) random.randn ->  generates samples from the standard normal distribution (mean = 0, variance = 1). 
# It can create arrays of specified shapes filled with random values.
ar2 = np.random.randn(2,3,3)
print(ar2)
# c) random.randint -> generates an integer of random values of matrix of the specified size
ar3 = np.random.randint(1,10,size=[1,3,3])
print(ar3)


# -------------------------------------------------------------------------------------------------------

# 3. Numpy Data Types and Type Casting
# Creating a normal numpy array without using any inbuilt functions
ar4 = np.array([1,2,3.0,4]) # Changing the data type of even one value will change the data type of all other values too
print(ar4)
# Creating a numpy array from an already existing list
lst = [1,2,3,4.0,"Me"]
ar5 = np.array(lst)
print(ar5)
# To check the data type of the values inside the numpy array: dtype
# To check the Type of the variable containing the numpy array: type()
print(type(ar4),ar4.dtype)
# To change the data type
ar6 = np.array([1,2.4,2.8,6.7],dtype=int)
print(ar6)
#Type Casting -> Using astype()
arr = np.array([1,2,3])
print(arr.dtype)
new_arr = arr.astype(float)
print(new_arr,new_arr.dtype)
# Type Casting Error
ar7 = np.array([1,2,"Me"])
print(ar7.dtype)
ar8 = np.array([1,2,3])
print(ar8.astype(str))
# Type Conversion of a String Value to Integer or Float is not possible
# new_ar7 = ar7.astype(int) 
# print(new_ar7)


# -------------------------------------------------------------------------------------------------------

# 3. Array Reshaping -> To change the shape of an array without changing the data present in it.
# a) Using reshape()
# Using -1 for Inference
#You can use -1 as one of the dimensions to let NumPy automatically 
#calculate its value based on the other dimensions.
ar_new = np.array([10,20,30,40,50,60])  
arr_2d = ar_new.reshape(-1,3 )
print(arr_2d)
ar9 = np.array([1,2,3,4,5,6])
rshp_arr = ar9.reshape(2,3)
print("Reshape with reshape()")
print(rshp_arr)
reshape2 = rshp_arr.reshape(1,2,3)
print(reshape2)
# b) Using ravel() -> Converts array of any dimension to a 1-D Array
rav = reshape2.ravel()
print("Reshape with ravel()")
print(rav)
print(reshape2)
rav[0]=100
print(rav)
print(reshape2)
# c) Using flatten() -> This too converts the array of any dimesnion to a 1-D Array
new_array = np.array([5,4,6,7,8,9])
flat = new_array.flatten()
print("Reshape with flatten()")
print(flat)
print(new_array)
flat[0]=1
print(flat)
print(new_array)
# Note the major difference between flatten() ravel() is :
# ravel() -> Creates a view i.e. any difference made in the ravelled array will reflect in the original one.
# flatten() -> Creates a copy i.e. any difference made in the flattened array would not be reflected 
# in the original one.
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
# Addition
add = a+b
# Subtraction
sub = a - b
# Multiplication
mul = a*b
# Division
div = b/a
div_floor = b//a # Integer Division
# Remainder
rem = b%a
# Exponents
exp = a**a
print(f"Addition: ",add,"\n","Subtraction: ",sub,"\n","Multiplcation: ",mul,"\n","Division: ",div,"\n","Floor Division: ",div_floor,"\n",
      "Remainder: ",rem,"\n","Exponent ",exp,"\n",)
# Universal Functions -> ufuncs
# a) SquareRoot -> np.sqrt
c = np.array([4,6,9,16])
square_root = np.sqrt(c)
print(f"Array containing squares: ",c,"\n","Array containing square roots: ",square_root)
# b) Exponential -> e^x calculation
d = np.exp([1,2])# e^1 and e^2
print(f"The exponential function usage is: ",d)

# ----------------------------------------------------------------------------------------------------------------

# Indexing and Slicing
# Same as that in lists, just remember to put the step value while trying to get the last values through
# negative indexing, e.g. [-1:-4:-1]
g = np.array([1,2,3,4,5])
print("Indexing and Slicing Negative Indexing usage of Step value explanation")
print(g[-1:-4:-1],"\n")
print(g[-1:-4])
print("Normal Indexing and Slicing")
print(g[::2])
# Multidimensional Slicing and Indexing
matrix = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
print("Outputs for Multidimensional Slicng")
print(matrix[0:2,:]) # Same as matrix[0:2,0:3]
# Remember the first one is layer/row,  then column and so on
# To print 5,6,8,9
print(matrix[1:3,1:3])
print(matrix[1,:]) # It means only one row to be included
print(matrix[:,2]) # It means only one column to be included
# np.take(arr,index) -> Built in function to perform indexing and slicing
c = np.array([10,20,30,40,50,60])
print("Outputs for np.take() built in function")
print(np.take(c,[0,1,2,3,4,5]))

# ----------------------------------------------------------------------------------------------------------------

# Transpose of a Matrix: The rows are replaced by the columns and vice versa. It is carried out by using
# arr.T ar arr.transpose()
t = np.array([[1,2,3,],
              [5,6,7],
              [8,9,10]])
transpose = t.T
print("Output for Transpose of a 2-d array")
print(transpose)

# ----------------------------------------------------------------------------------------------------------------

# Concatenation and Stacking in Numpy Arrays: 
# a) Concatenation : It is the joining of multiple arrays together.
c1 = np.array([1,2])
c2 = np.array([3,4])
concatenate = np.concatenate([c1,c2])
print("Output of concatenate() function")
print(concatenate)
# b) np.hstack() : stacks arrays horizontally (column-wise). For 2D arrays, it concatenates along axis=1.  
# For 1D arrays, it simply concatenates them into a longer 1D array. 
a1 = np.array([1, 2, 3])
b1 = np.array([4, 5, 6])
print(" Output for np.hstack() function")
# Horizontal stack (1D → 1D)
print(np.hstack((a1, b1)))
a2 = np.array([[1, 2], [3, 4]])
b2 = np.array([[5, 6], [7, 8]])
# Horizontal Stack (2D) :  Columns Increase
print(np.hstack((a2, b2)))
# c) np.vstack() : stacks arrays vertically (row-wise). For 2D arrays, it concatenates along axis=0.  
# For 1D arrays, you must reshape them into 2D before stacking.
print(" Output for np.vstack() function")
# Vertical stack (requires reshape to 2D for a 1D array implementation)
print(np.vstack((a1.reshape(1, -1), b1.reshape(1, -1))))
# For 2D arrays: rows increase
print(np.vstack((a2, b2)))
# stack((arr1,arr2),stack = 0/1)-> To perform the operations without hstck or vstack.
# axis = 0 -> vstack (Stacking will be carried out row-wise).
# axis = 1 -> hstack (Stacking will be carried out column-wise).
#axis=0 → downward → adds more rows
#axis=1 → sideways → adds more columns

# ----------------------------------------------------------------------------------------------------------------

# Aggregate Functions:
agg = np.array([1,2,3])
print("Aggregate Functions Output")
# a) np.sum():
print(np.sum(agg))
# b) np.mean():
print(np.mean(agg))
# c) np.median():
print(np.median(agg))
# d) np.std():
print(np.std(agg))
# e) np.var():
print(np.var(agg))
# f) np.max():
print(np.max(agg))
# g) np.min():
print(np.min(agg))
arg_example = np.array([
    [10, 50, 30],
    [40, 20, 60]
])
# axis=0 → column-wise
print(np.argmax(arg_example, axis=0))
# [1, 0, 1]
# Column 0 → 40 → row 1
# Column 1 → 50 → row 0
# Column 2 → 60 → row 1
# axis=1 → row-wise
print(np.argmax(arg_example, axis=1))
# [1, 2]
# Row 0 → 50 → column 1
# Row 1 → 60 → column 2
# Same concept applies to argmin()

# ----------------------------------------------------------------------------------------------------------------

# Conditional Based Operations: np.where()
ar_con = np.array([10, 5, 20, 3])
result = np.where(ar_con > 10, 1, 0)
print("np.where() output")
print(result)

# ----------------------------------------------------------------------------------------------------------------

# Masking: Using a condition to select specific elements from an array
print("Masking Outputs")
arr_mask = np.array([10, 5, 20, 3, 15])
# 1. Basic Masking
# Select values greater than 10
print(arr_mask[arr_mask > 10])
# [20 15]
# 2. Masking with Multiple Conditions
# Select values greater than 5 AND less than 20
print(arr_mask[(arr_mask > 5) & (arr_mask < 20)])
# [10 15]
# 3. Masking with 2D Array
# Select all values greater than 30
arr_mask2 = np.array([
    [10, 50, 30],
    [40, 20, 60]
])
print(arr_mask2[arr_mask2 > 30])
# [50 40 60]

# ----------------------------------------------------------------------------------------------------------------

# Broadcasting: Broadcasting allows NumPy to perform operations on arrays with different shapes.
# Rules:
# 1. Compare shapes from RIGHT to LEFT.
# 2. Dimensions are compatible if they are equal OR one is 1.
# 3. Result shape takes the larger dimension.
# 4. If dimensions are different and neither is 1 → Error.
# ----------------------------------------------------------
# 1. Scalar Broadcasting
# ----------------------------------------------------------
print("Broadcasting Outputs")
arr_broad = np.array([10, 20, 30])
print(arr_broad + 5)
# [15 25 35]
# Scalar 5 is applied to every element.
# ----------------------------------------------------------
# 2. 2D Array + 1D Array
# ----------------------------------------------------------
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
x = np.array([1, 2, 3])
print(arr + x)
# [[11 22 33]
#  [41 52 63]]
# Shapes:
# arr → (2, 3)
# x   → (3,) → treated as (1, 3)
#
# Result → (2, 3)
# ----------------------------------------------------------
# 3. Broadcasting with a Column
# ----------------------------------------------------------
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
x = np.array([
    [1],
    [2]
])
print(arr + x)
# [[11 21 31]
#  [42 52 62]]
# Shapes:
# arr → (2, 3)
# x   → (2, 1)
#
# Result → (2, 3)
# ----------------------------------------------------------
# 4. Broadcasting Error
# ----------------------------------------------------------
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
b = np.array([10, 20])
# print(a + b)   # ValueError
# Shapes:
# a → (2, 3)
# b → (2,)
#
# Compare from right:
# 3 vs 2 → incompatible ❌
# Therefore broadcasting is not possible.

# ----------------------------------------------------------------------------------------------------------------

# Vectorization:
import numpy as np
# 1. Vectorized Arithmetic
arr = np.array([10, 20, 30])
print(arr * 2)
# [20 40 60]
# 2. Vectorized Operation on Two Arrays
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print(a + b)
# [11 22 33]
# 3. Vectorized Comparison + Masking
arr = np.array([10, 5, 20, 3, 15])
print(arr[arr > 10])
# [20 15]
# 4. Vectorization + Broadcasting
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
x = np.array([1, 2, 3])
print(arr + x)
# [[11 22 33]
#  [41 52 63]]











