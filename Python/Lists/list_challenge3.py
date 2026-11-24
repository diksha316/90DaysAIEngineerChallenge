# 5. Remove Duplicates
# Hint: Create an empty list. For each number, check whether it is already in your new list. Only append it if it isn't.
numbers = [1, 2, 2, 3, 4, 3, 5, 1, 6]
new_list = []

# 2. Using a for loop
for i in numbers:
        if i not in new_list:
            new_list.append(i)
        # else:
        #     continue
print(new_list)

# 1. Using set() 
# unique_item = set()

# for n in numbers:
#     if n in unique_item:
#         print("Duplicate found: ",n)
#     unique_item.add(n)
# print(unique_item)


