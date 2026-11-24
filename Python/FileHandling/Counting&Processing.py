#1. Count the total number of lines in a file.
count = 0
with open("my_details.txt","r") as f:
    # Using readlines
    data = f.readlines()
    lines = len(data)
    print("The number of lines in this file is: ",lines)
    f.seek(0)
    # Using for loop
    for line in f:
        count += 1
print("Total number of lines in this file are: ",count)

#2. Count the total number of words in a file.
with open("my_details.txt","r") as f:
    data = f.read()
    list_data = data.split()#will split the string read on the basis of whitespaces
    print("the number of words in the file are: ",len(list_data))

#3. Count the total number of characters in a file including whitespaces.
with open("my_details.txt","r") as f:
    data= f.read()
    print("The number of chracters in the file including whitespaces are: ",len(data.replace("\n","")))

#4. Count the number of vowels in a text file.
count_vowel = 0
vowels = "aeiouAEIOU"
with open("my_details.txt","r",encoding="utf-8")as f:
    for line in f:
        for char in line:
            if char in vowels:
                count_vowel+=1
    print("The number of vowels in this file are: ",count_vowel)

#5. Count how many times each character appears in a file.
char_count = {}
with open("my_details.txt","r") as f:
    for line in f:
        for char in line:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
print(char_count)
            
#6. Search for a particular word in a file and report whether it exists.
with open("my_details.txt","r") as f:
    data2 = f.read()
    cleaned_data = data2.split()
    print(cleaned_data)
    for word in cleaned_data:
        if word == "Diksha":
            print("Found")
        else:
            continue

#7. Count how many times a given word appears in a file.
word_count = {}
with open("my_details.txt","r")as f:
    content = f.read()
    cleaned_content = content.split()
    for word in cleaned_content:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
print(word_count)

#8. Find and print the longest line in a text file.
with open("my_details.txt","r")as f:
    new_data = f.readlines()
    line_length = []
    for string in new_data:
        line_length.append(len(string))
    print(line_length)
    longest = line_length[0]
    for i in line_length:
        if i> longest:
            longest = i
    print(longest)

        