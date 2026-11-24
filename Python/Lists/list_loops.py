numbers = [10, 20, 30, 40, 50]
list_sum = 0
#list_average = 0
count = 0
count_even = 0 

#1. Calculate the sum using a loop, without using sum()
for  i in numbers:
    list_sum += i
print(list_sum)

#2. Calculate the average.
list_average = list_sum / (len(numbers))
print(list_average)

#3. Count how many numbers are greater than 25.
for i in numbers:
    if i > 25:
        count += 1
print("The numbers which are greater than 25 in the list of numbers are: ",count)

#4. Count how many numbers are even.
for i in numbers:
    if i % 2 == 0:
        count_even+=1
print("The count of even numbers in the list is: ", count_even)