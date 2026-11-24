import numpy as np

# Level 1 - Numpy Fundamentals ----------------------------------------------------------------------------------------------------

# 1. Create a NumPy array
arr = np.array([10,20,30,40,50])

# 2. Check array properties
print(np.ndim(arr)) # Dimension
print(np.shape(arr)) # Shape
print(np.size(arr)) # Size
print(arr.dtype) # Data Type

# 3. Create a 2D array
arr_2D = np.array([[10,20,30],
                   [40,50,60],
                   [70,80,90]])
print(np.ndim(arr_2D)) # Dimension
print(np.shape(arr_2D)) # Shape
print(np.size(arr_2D)) # Size

# 4. Create arrays using NumPy functions
# a) An array of 10 zeros
print(np.zeros(10,dtype=int))
# b) An array of 5 ones
print(np.ones(5,dtype=int))
# c) Numbers from 1 to 20 -> Using arange()
print(np.arange(1,21,dtype=int))
# d) 6 evenly spaced numbers between 0 and 10 -> Uisng linspace()
print(np.linspace(0,10,6,dtype=int))

# 5. Reshape an array
arr_one = np.arange(1,13)
print(arr_one)
# a) Create numbers from 1 to 12 and reshape them into: 3X4
reshaped = arr_one.reshape([3,4])
print(reshaped)
# b) Then reshape the same array into: 2x6
reshape2 = reshaped.reshape([2,6])
print(reshape2)


# Level 2 - Indexing and Slicing ----------------------------------------------------------------------------------------------------

# 1. Basic Indexing
arr = np.array([10, 20, 30, 40, 50])
# First element
print(arr[0])
# Last Element
print(arr[-1])
# Third Element
print(arr[2])
# Second-Last Element
print(arr[-2])

# 2. Array Slicing
# a) Using the same array, extract: [20,30,40]
print(arr[1:-1])
# b) Using the same array, extract: [10,30,50]
print(arr[::2])

# 3. Reverse an Array: Reverse the array using slicing
print(arr[::-1]) # Remember

# 4. 2D Indexing
arr_new_2D = np.array([[10,20,30],
                      [40,50,60],
                      [70,80,90]])
# Find 50, 90 and 20
print(f"The number 50 -",arr_new_2D[1,1]," The number 90 -",arr_new_2D[2,2]," The number 20-",arr_new_2D[0,2])
# Entire second row:
print(f"The entire second row- \n",arr_new_2D[1,:]) # Remember                                 
# Entire third column:
print(f"The entire third column- \n",arr_new_2D[:,2]) # Remember


# Level 3 - Array Operations ----------------------------------------------------------------------------------------------------

# 1. Arithmetic Operations :
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])
# Addition:
print(a+b)
# Subtraction
print(a-b)
# Multiplication
print(a*b)
# Division
print(a/b)
# a to the power 2
print(a**2)

# 2. Aggregate Functions
arr = np.array([10, 20, 30, 40, 50])
# Sum
print(np.sum(arr))
# Mean
print(np.mean(arr,dtype=int))
# Minimum
print(np.min(arr))
# Maximum
print(np.max(arr))
# Standard Deviation
print(np.std(arr))
# Variance
print(np.var(arr))

# 3. Aggregation on 2D Arrays:
# a) Sum of entire array
print(np.sum(arr_new_2D))
# b) Sum of each column
print(np.sum(arr_new_2D,axis=0))
# c) Sum of each row
print(np.sum(arr_new_2D,axis=1))
# d) Mean of each column
print(np.mean(arr_new_2D,axis=0))
# e) Mean of each row
print(np.mean(arr_new_2D,axis=1))
# f) Sum of 2nd row
print(np.sum([arr_new_2D[1,:]])) # Remember

# 4. argmax() and argmin() -> Just normally go through the notes


# Level 4 - Boolean Operations and Masking ----------------------------------------------------------------------------------------------------

# 1. Find Values greater than a particular Number :
arr = np.array([10, 5, 20, 3, 15, 8,25])
# Extract all values greater than 10
print(arr[(arr>10)])

# 2. Multiple conditions
# greater than 5 AND less than 20
print(arr[(arr>5) & (arr<20)]) # Remember to put the conditions in different brackets
# OR Condition - less than 5 OR greater than 20
print(arr[(arr<5) | (arr>20)]) 

# 3. Replace values using Masking
arr = np.array([10, 20, 30, 40, 50])
# Replace every value greater than 30 with 0
new_arr = np.where(arr>30 , 0 , arr)
print(new_arr)

# 4. Find the number of values which are greater than 10
print(np.size(arr[(arr>10)]))


# Level 5 - where() ----------------------------------------------------------------------------------------------------

# 1. Replace values using np.where():
# Replace values greater than 30 with 1, otherwise 0
arr = np.array([10, 20, 30, 40, 50])
print(np.where(arr>30,1,0))

# Categorize Values
marks = np.array([35, 55, 75, 90, 25])
# 1 → marks >= 50 , 0 → marks < 50
print(np.where((marks>=50),1,0))


# Level 6 - Broadcasting ----------------------------------------------------------------------------------------------------

# 1. Scalar Broadcasting
arr = np.array([10, 20, 30])
# arr+10
print(arr+10)
# arr-5
print(arr-5)
# arr*2
print(arr*2)

# 2. 2D + 1D Broadcasting
arr_2D = np.array([[10,20,30],
                   [40,50,60]])
arr = [1,2,3]
# Add 1 2 3
print(arr_2D+arr)

# 3. Row / Column Broadcasting
# Add 1
#     2 Using a column vector
Col_vec = np.array([[1],
          [2]])
print(arr_2D+Col_vec)


# Level 7 - Vectorization ----------------------------------------------------------------------------------------------------

# 1. Convert a loop into a vectorized code
arr = np.array([10, 20, 30, 40, 50])
mul = []
# Code to multiply every value by 2
for i in arr:
    mul = arr*2
print(mul)
print(arr*2)

# 2. Vectorized Calculation
price = np.array([100, 200, 300, 400])
quantity = np.array([2, 3, 1, 4])
# Calculate the total price for each product using vectorized operations.
print(f"The Total Price is : ",price*quantity)

# 3. ML-style vectorization
X = np.array([
    [10, 20, 30],
    [20, 30, 40],
    [30, 40, 50]
])
# Subtract
mean = np.array([20, 30, 40])
print(X-mean)


# Level 8 - Concatenation and Stacking ----------------------------------------------------------------------------------------------------

# 1. Concatenate Arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.concatenate([a,b]))

# 2. Vertical vs Horizontal Stacking -> Check the notes


# Level 9 - Random and ML Data ----------------------------------------------------------------------------------------------------

#2. random.seed() -> Important and Remember
#print(np.random.seed(42)) #When you set a specific seed value, the sequence of random numbers generated  
# will remain consistent across runs. This is particularly helpful in scenarios like  
# machine learning experiments or simulations where reproducibility is critical.

# 1. Generate Random Data
# a) 10 random numbers between 0 and 1
random1 = np.random.rand(10) # It will take the shape of the output here -> Remember
print(random1)
# b) a 3X3 matrix
random2 = np.random.rand(3,3)
print(random2)
# c) 10 random integers between 1 and 100
random3 = np.random.randint(1,101,size=100) # It will take the shape of the output in size -> Remember
print(random3)
# 2. Vertical vs Horizontal Stacking -> Check the notes


# Level 9 - AI Engineer Mini Problems ----------------------------------------------------------------------------------------------------

# 1. Featue Normalization
X = np.array([10, 20, 30, 40, 50])
# Perform min-max normalization
X_min = np.min(X)
X_max = np.max(X)
X_normalized = (X - X_min) / (X_max - X_min)
print(X_normalized)

# 2. Find the best prediction
probabilities = np.array([
    [0.1, 0.7, 0.2],
    [0.8, 0.1, 0.1],
    [0.2, 0.3, 0.5]
])








