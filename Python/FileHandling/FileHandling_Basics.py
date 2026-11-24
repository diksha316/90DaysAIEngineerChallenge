#1. Create a text file named my_details.txt and write your name, target role, and programming language into it.
with open("my_details.txt","w") as f:
    f.write("Name -> Diksha Jaiswal \nTarget Role -> AI/GEN AI Engineer \nProgramming Language -> Python")

#2, Open my_details.txt and print its entire content.
with open("my_details.txt","r") as f:
    read = f.read()
    print(read)

#3. Read and print only the first 10 characters of a file.
with open("my_details.txt","r") as f:
    read_ten = f.read(10)
    print(read_ten)

#4. Read and print only the first line using readline().
with open("my_details.txt","r") as f:
    read_one_line = f.readline()
    print(read_one_line)

#5. Read all lines using readlines() and print the resulting list.
with open("my_details.txt","r") as f:
    read_lines = f.readlines()
    print(read_lines)

#6. Print the number of characters in a text file.
with open("my_details.txt","r") as f:
    content_char = f.read()
    char_count = len(content_char)
    print(f"The number of characters with the trailing white spaces and the new line character in this file are:  {char_count}")
    # Without the newline caharcter and the trailing whitespaces
    cleaned_count = len(content_char.replace(" ",""))
    count_without_newlinecharacter = len(content_char.replace("\n",""))
    print(f"The count of the characters without trailing spaces is {cleaned_count}")
    print(f"The count of the characters without newline character is {count_without_newlinecharacter}")

#7. Use tell() to display the current file pointer position after reading some characters.
with open("my_details.txt","r") as f:
    print(f.tell())
    data = f.readline()
    print(data)
    print(f.tell())
    data_1 = f.read()
    print(data_1)
    f.seek(2)
    #print(data)
   
    
    
