# 6: Find the second-largest distinct number

# If the current number is greater than the largest number found so far,
# the previous largest number becomes the second-largest number.
# Then, update largest with the current number.
# IMPORTANT: Update second_largest BEFORE updating largest,
# otherwise both variables will contain the same value.

numbers = [10, 25, 8, 25, 18, 10, 21]
largest = numbers[0]
second_largest = numbers[0]

for i in numbers:
    if i>largest:
        second_largest = largest  # Store the previous largest value
        largest = i  # Update largest with the current number
    elif (i < largest and i > second_largest):
        second_largest = i  # Update second-largest if the number is between them

print(second_largest)      

