import pandas as pd

# 1. Read employees.csv into a DataFrame called: df
df = pd.read_csv("employees.csv")

# 2. Inspect
# first 3 rows
print(df.head(3))
# last 2 rows
print(df.tail(2))
# shape
print(df.shape)
# column names
print(df.columns)
# data types
print(df.dtypes)
# info
df.info()
# describe
df.describe()

# 3. Export
df.to_csv("employees_backup.csv",index=False)

# 4. JSON - Convert the same dataframe to JSON
df.to_json("employees.json",orient="records")

# 5. EXCEL - Convert the same dataframe to excel
df.to_excel("employees.xlsx",index=False)

# 6. Find the nunmber of evaluation examples from evaluation.csv after performing all the tasks

# a) Read the CSV
new_df = pd.read_csv("evaluation.csv")
# b) Display the first 2 rows
print(new_df.head(2))
# c) Find the number of evaluation examples,
print(new_df.shape[0])
# d) Display the column names.
print(new_df.columns)
# e) Display the data types.
print(new_df.dtypes)
# f) Save it as evaluation_backup.csv without the index.
new_df.to_csv("evaluation_backup.csv",index=False)
# g) Save it as evaluation.json
new_df.to_json("evaluation.json",orient="records")