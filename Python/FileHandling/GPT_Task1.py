with open("my_details.txt","w") as f :
    f.write("Name -> Diksha Jaiswal \nTarget Role -> GEN AI Developer/ Engineer or AI Engineer \nCurrent Programming Language -> Python")


with open("my_details.txt","r") as f:
    string_list = f.readlines()
    print(string_list)
    #data = f.read()
    #data2= f.read(20)
    #data3 = f.readline()
    #print(data3)
    #print(data2)
    #print(data)
    