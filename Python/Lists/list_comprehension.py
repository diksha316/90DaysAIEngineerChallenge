numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#List Comprehension Syntax -> [expression for item in iterable if condition]

#1. Create a list of squares of all numbers.
squared_nums = [x*x for x in numbers]
print(squared_nums)

#2. Create a list containing only even numbers.
even_nums = [x for x in numbers if x%2 ==0]
print(even_nums)

#3. Create a list of squares of only the even numbers.
squared_even_nums = [x*x for x in numbers if x%2 ==0]
print(squared_even_nums)


# # Using Loops
# #1. Create a list of squares of all numbers.
# for i in numbers:
#     squared_nums.append(i*i)
# print(squared_nums)

# #2. Create a list containing only even numbers.
# for i in numbers:
#     if i % 2 == 0:
#         even_nums.append(i)
# print(even_nums)

# #3. Create a list of squares of only the even numbers.
# for i in numbers:
#     if i%2 == 0:
#         squared_even_nums.append(i*i)
# print(squared_even_nums)