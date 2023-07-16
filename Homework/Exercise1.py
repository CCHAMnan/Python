#Create class
class Employee: 
    #constructor
    def __init__(self, id, name, gender, salary):
        self.id = id
        self.name = name
        self.gender = gender
        self.salary = salary

    #function to read employee by user input
    def read_employee():
        id = int(input("Enter ID: "))
        name = input("Enter name: ")
        gender = input("Enter gender(F/M): ")
        salary = int(input("Enter Salary: "))
        return Employee(id, name, gender, salary)

    #function to add employee details to the "Employee.txt" file
    def add_employee(self):
        #open file as append
        with open("Employee.txt","a") as file:
            file.write(f"{self.id}, {self.name}, {self.gender}, {self.salary}\n")

    #function to delete employee from the file
    def delete_employee(self, id):
        employees = []
        #open file as read
        with open("Employee.txt","r") as file:
            for line in file:
                data = line.split(",")
                #check if file has the employee id
                if data[0] != str(id):
                    employees.append(line)
        #open file as write
        with open("Employee.txt","w") as file:
            for employee in employees:
                file.write(employee)

#function to search employee
def search_employee(id):
    #open file as read
    with open("Employee.txt","r") as file:
        #list of key with its value
        data = file.read().rstrip("\n").split("\n") 
        dict1 = {}
        for i in data:
            i = i.split(", ")
            #seperate each key and value
            dict1[i[0]] = {'name': i[1], 'gender': i[2], 'salary': i[3]}

        #check if employee id is in dictionary
        if str(id) in dict1:
            #store the value of a key
            temp = dict1[str(id)]
            print("-------------------------------------")
            print("ID   Name         Gender       Salary")
            print("-------------------------------------")
            print(
                str(id).ljust(4),
                temp['name'].ljust(14),
                temp['gender'].ljust(10),
                temp['salary'].ljust(10)
            )       
            print("-------------------------------------")    
        else:
            print("Search Not Found")     

#function to display all the employee in the file
def display_all():
    #open file as read
    with open("Employee.txt","r") as file:
        #list of key with its value
        data = file.read().rstrip("\n").split("\n") 
        dict1 = {}
        for i in data:
            i = i.split(", ")
            dict1[i[0]] = {'name': i[1], 'gender': i[2], 'salary': i[3]}

        #sort the dictionary by id
        sort_dict = sorted(dict1.items(), key=lambda x:x[0])
        #convert the sorted list back to dictionary
        convert_dict = dict(sort_dict)

        #display the whole dictionary by formatting
        for line in convert_dict.items():
            temp = convert_dict[line[0]]
            print(
                line[0].ljust(4),
                temp['name'].ljust(14),
                temp['gender'].ljust(10),
                temp['salary'].ljust(10)
            )

#store 3 random Employee into the file
emp1 = Employee(1, "Lina", "F", 1000)
emp2 = Employee(2, "Pheaktra", "F", 900)
emp3 = Employee(3, "Sing", "M", 800)
with open("Employee.txt","w") as file:
    file.write(f"{emp1.id}, {emp1.name}, {emp1.gender}, {emp1.salary}\n")
    file.write(f"{emp2.id}, {emp2.name}, {emp2.gender}, {emp2.salary}\n")
    file.write(f"{emp3.id}, {emp3.name}, {emp3.gender}, {emp3.salary}\n") 

#Main
while True:
    print("""
a. Add new employee
b. Delete employee by id
c. Search employee by id
d. Display all employee
e. Exit program 
    """)

    menu = str(input("Select a menu: "))
    employee = Employee("","","","")

    if menu == 'a':
        #call read_employee function to insert employee details
        employee = Employee.read_employee()
        #call add_employee function to add employee details into the file
        employee.add_employee()

    elif menu == 'b':
        employee_id = int(input("Enter employee_id: "))
        #call delete_employee() function to delete an employee by id
        employee.delete_employee(employee_id)

    elif menu == 'c':
        employee_id = int(input("Enter employee_id: "))
        #call search_employee() function to search for an employee by id
        search_employee(employee_id)

    elif menu == 'd':
        #call display_all() function to diplay all employee details from the file
        print("-------------------------------------")
        print("ID   Name         Gender       Salary")
        print("-------------------------------------")
        display_all()
        print("-------------------------------------")

    elif menu == 'e':
        #Exist the program
        break
    else:
        print("Error! Please select menu from a to e.")