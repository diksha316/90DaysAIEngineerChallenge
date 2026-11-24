# 4: Find the largest number
# Hint: Assume the first element is the largest initially. Compare each remaining element against it

numbers = [14, 67, 23, 89, 45, 32]
largest = numbers[0]

for i in numbers:
    if i>largest:
        largest = i
print(largest)
