matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sum = 0

#1. Print every element using nested loops.

for i in matrix:
    for j in i:
        print(j)

#2. Calculate the sum of all elements.
for row in matrix:
    for number in row:
        sum += number
print(sum)

#3. 