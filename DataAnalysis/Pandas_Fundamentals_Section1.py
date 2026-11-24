import pandas as pd

# 1. Create a pandas series containing:
series1= pd.Series([10, 20, 30, 40, 50])
print("Pandas Series is: ",series1)

# 2. Create a dataframe:
dict1 = {
    "Name" : ["A","B","C"],
    "Age" : [20,21,22],
    "Salary" : [40000,50000,60000]
}
df = pd.DataFrame(dict1)
print("Pandas DataFrame is: ",df)

# 3. Print the first 3 rows of df.
print(df.head(3))

# 4. Print the last 2 rows of df.
print(df.tail(2))

# 5. Display 2 random rows from df.
print(df.sample(2))

# 6. Find the number of rows and columns.
print(f"No of Rows = ",df.shape[0],"\n","No of Columns = ",df.shape[1])

# 7. Print all Column names
print(f"The columns are: ",list(df.columns))

# 8. Print the DataFrame's data types.
print("The datatypes of the columns are : ",df.dtypes)

# 9. Display the information about the DataFrame using info()
print(df.info())

# 10. Generate the statistical summary using describe()
print(df.describe())

# 11. Difference between df["Age"] and df[["Age"]] 
print(type(df["Age"]))
print(type(df[["Age"]]))

# 12. Find the data type of the Salary column.
print(df["Salary"].dtypes) # Remember

# 13. Find the data type of the Name column.
print(df["Name"].dtypes) # Remember


