with open("practice2.txt","r") as f:
    data = f.read()
    print(data)

numbers = data.split(",")
cleaned_numbers = [nums.replace("\n","") for nums in numbers]
print(numbers)
print(cleaned_numbers)
count_even =0

for i in cleaned_numbers:
    if (int(i) % 2 == 0):#As the data is in the string format in the list therefore it must be converted to integer first
        count_even += 1

print("The number of even numbers in the file are:", count_even)

