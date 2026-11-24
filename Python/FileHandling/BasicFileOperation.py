#1. File Opening and Reading the data from it (Text files)
f = open("C:\\Users\\Diksha.Jaiswal\\Documents\\Invoice Processing AI Agent Requirements.txt","r")
data = f.read()
print(data)
print(type(data))

#2. Reading only 10 characters from the file:
# char5 = f.read(10)
# print(char5)# output will come as an empty newline without the seek() method

#3. Reading only one line from the file
f.seek(0)
line1 = f.readline()
print(line1)

# To perform all of these operations simultaneously we need to use seek(0) method or the output will be
# an empty string because the first read() method will read the entire file and then the pointer will be
# set at the end of the file therefore we need to set the pointer to the file, back to the start of
# the file again.

