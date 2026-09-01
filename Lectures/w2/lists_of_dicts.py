# Working with lists and lists of dictionaries.
# Andrew Huff - 9/1/26

# Current Issue(s)
# 1. Removing from the list

# List of employees
employees = [{}]

# Function that adds employees to the list
def add_employee(name, salary):
    emp = {
        "name": name,
        "salary": salary
    }
    employees.append(emp)

# Function that removes employees to the list
def remove_employee(name):
    for i, emp in enumerate(employees):
        employees.pop() # pop at a certain index
        # print(employees)

# Function to install access control to employees
def finance_related_function():
    pass

# Beginning of program
while True:
    option = input("Press 1 to Add, 2 to Remove, q to Quit \n")
    # Add an employee
    if option == '1':
        name = input("Enter employee name: ")
        salary = input("Enter employee salary: ")
        add_employee(name, salary)
        print("Update successful!")
    # Remove an employee
    if option == '2':
        name = input("Enter a name to remove: ")
        remove_employee(name)
        print("Update successful!")
    # Terminate the program
    if option == 'q':
        break

print(employees)
# for i in range(3):
#    name = input("Enter employee name: ")
#    remove_employee(name)
    #salary = float(input("Enter employee salary: "))
    #add_employee(name, salary)