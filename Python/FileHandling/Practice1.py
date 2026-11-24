# Create a new file "practice1.txt" using python and add the following data into it:
# Hi Everyone
# We are laerning File I/O 
# using Java
# I like programming in Java
# WAF to replace all the occurences of "Java" with "Python" in the file
# Search if the word "learning" exists in teh file or not? 
# Also find the line at which the word "learning" was found at first. 

with open("practice1.txt","r") as f :
    data = f.read()

new_data = data.replace("Java","Python")
print(new_data)

with open("practice1.txt","w") as f:
    f.write(new_data)

search_word = "learning"
with open("practice1.txt","r") as f:
    data1 = f.read()
    if (data1.find(search_word) != -1) :
        print("Found")
    else:
        print("Not found")


data2 = True # As we are going to read line by line, so we need to see when is the data getting over in a document
line_number = 1
with open("practice1.txt","r") as f:
    while data2:
        data2 = f.readline()
        if(search_word in data2):
            print(line_number)
        line_number += 1    


