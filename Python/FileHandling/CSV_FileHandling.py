import csv

#1. Read a CSV file using csv.reader() and print each row.
with open("C:\\Users\\Diksha.Jaiswal\\Downloads\\employees_practice.csv","r") as f:
    employee_data = csv.reader(f,delimiter=',')
    #print(employee_data) can't do this
    for data in employee_data:
        print(data)

#2. Read a CSV file using csv.DictReader() and access values by column name.
with open("C:\\Users\\Diksha.Jaiswal\\Downloads\\employees_practice.csv","r") as f:
    employee_data_2 = csv.DictReader(f,delimiter=',')
    #print(employee_data) can't do this
    for data in employee_data_2:
        print(data)

#3. Filter and print employees belonging to the Engineering department.
with open("C:\\Users\\Diksha.Jaiswal\\Downloads\\employees_practice.csv","r") as f:
    employee_data_3 = csv.DictReader(f,delimiter=',')
    for data in employee_data_3:
        if data['department'] == 'Engineering':
            print(data)

#4. Calculate the total and average salary of employees in a CSV file.
total_salary = 0
average = 0
count = 0
with open("C:\\Users\\Diksha.Jaiswal\\Downloads\\employees_practice.csv","r") as f:
    employee_data_4 = csv.DictReader(f,delimiter=',')
    for data in employee_data_4:
            total_salary += int(data['salary'])
            count+=1
    average = total_salary/count
    print(average)

#5. Write a list of employee dictionaries into a CSV file using csv.DictWriter().
employees_list = [{'name': 'Aarav', 'department': 'Engineering', 'salary': '75000'},
{'name': 'Priya', 'department': 'HR', 'salary': '62000'},
{'name': 'Rahul', 'department': 'Engineering', 'salary': '82000'},
{'name': 'Sneha', 'department': 'Finance', 'salary': '68000'},
{'name': 'Arjun', 'department': 'Engineering', 'salary': '91000'},
{'name': 'Meera', 'department': 'Marketing', 'salary': '65000'},
{'name': 'Vikram', 'department': 'Engineering', 'salary': '78000'},
{'name': 'Ananya', 'department': 'HR', 'salary': '59000'},
{'name': 'Aarav', 'department': 'Engineering', 'salary': '75000'},
{'name': 'Rahul', 'department': 'Engineering', 'salary': '82000'},
{'name': 'Arjun', 'department': 'Engineering', 'salary': '91000'},
{'name': 'Vikram', 'department': 'Engineering', 'salary': '78000'}]
with open("C:\\Users\\Diksha.Jaiswal\\Downloads\\employees.csv","w")as f:
#         This tells Python:
# "I'm going to write dictionaries, and these are the column names."
        writer = csv.DictWriter(f, fieldnames=['name', 'department', 'salary'])
    
        writer.writeheader()#writes:name,department,salary
        writer.writerows(employees_list)#writes all the employee dictionaries into the CSV.
    

