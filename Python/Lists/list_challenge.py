# Seperate even and odd numbers from the list

numbers = [11, 24, 7, 18, 31, 42, 9, 16]
list_even = []
list_odd = []

for i in numbers:
    if i%2==0:
        list_even.append(i)
    else:
        list_odd.append(i)
print("List of even numbers: ", list_even)
print("List of odd numbers: ",list_odd)