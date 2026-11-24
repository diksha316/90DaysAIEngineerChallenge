import json

#1. Read a JSON file using json.load() and print its contents.
with open("C:\\Users\\Diksha.Jaiswal\\Downloads\\employees_practice.json","r")as f:
    d = json.load(f)
    print(d)
    print(type(d))

#2. Load JSON data and print an individual value, such as the person's name.
with open("C:\\Users\\Diksha.Jaiswal\\Downloads\\employees_practice.json","r")as f:
    d = json.load(f)
    print(d['person']['name'])
    #print(d['employees'])
    for employee in d["employees"]:
        print(employee['name'])



