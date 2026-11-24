list = [12, 5, 8, 20, 3, 15]

 # 1. Print the first and the last elements
print("The first element is: ", list[0],"\nThe last element is ",list[5])

 #2.  Print the first 3 elements
#for i in list:
    #print(i)
    #if list.index(i) == 2:
        #break
print(list[:3])

 #3.  Add 25 to the end of the list
list.append(25)
print(list)

 #4. Insert 10 at index 2 
list.insert(2,10)
print(list)

 #5. Remove the number 8 
list.remove(8)
print(list)

 #6. Final List and it's Length
print("The final list is: ", list, "\nThe length of the list is: ",len(list))


