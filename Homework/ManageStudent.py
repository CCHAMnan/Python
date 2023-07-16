# Create a class 
class Student:
    # Constructor
    def __init__(self, id, name, gender, dob, year, generation, degree, address, phone_no, email):
        self.id = id
        self.name = name
        self.gender = gender
        self.dob = dob
        self.year = year
        self.generation = generation
        self.degree = degree
        self.address = address
        self.phone_no = phone_no
        self.email = email

    # Add a new student to Student.txt file
    def add_student(self):
        read_file()
        id = input("Enter student ID: ")
        # Check to see if id in the dictionary
        while int(id) in student_dict:
            print("\nStudent ID already exists! Please enter a new student ID.")
            id = input("Enter student ID: ")

        name = input("Enter student's name: ")
        gender = input("Enter gender(M/F): ")
        dob = input("Enter date of birth(DD/MM/YYYY): ")
        year = input("Enter student's year: ")
        generation = input("Enter generation: ")
        degree = input("Enter degree: ")
        address = input("Enter student's address: ")
        phone_no = input("Enter Phone number: ")
        email = input("Enter email: ")

        # Add student details into Student class constructor
        student = Student(id, name, gender, dob, year, generation, degree, address, phone_no, email)
        student_dict[int(id)] = student

        #Copy the dictionary into a file
        write_to_file()

    # Seach for student by id and display their information
    def search_student(self, id):
        read_file()
        # Check to see if id in the dictionary
        while id not in student_dict:
            print("\nStudent not found.")
            id = int(input("Please Enter a new student ID: "))
        
        # Display the student details
        display_student(id)

    # Update student information
    def update_student(self):
        read_file()
        id = int(input("Enter student ID: "))
        # Check to see if id in the dictionary
        while id not in student_dict:
            print("\nStudent not found.")
            id = int(input("Please Enter a new student ID: "))
        
        name = input("Enter name: ")
        gender = input("Enter gender(M/F): ")
        dob = input("Enter date of birth(DD/MM/YYYY): ")
        year = input("Enter student's year: ")
        generation = input("Enter generation: ")
        degree = input("Enter degree: ")
        address = input("Enter student's address: ")
        phone_no = input("Enter Phone number: ")
        email = input("Enter email: ")

        # add all the arguments to the Student constructor
        student = Student(id, name, gender, dob, year, generation, degree, address, phone_no, email)
        student_dict.update({id: student})
        # Add dictionary to file
        write_to_file()
        print("\nStudent has been updated!")
            
            

    # Delete a student from Student.txt file
    def delete_student(self, id):
        read_file()
        # Check to see if id in the dictionary
        if id in student_dict:
            del student_dict[id]
            write_to_file()
            print("\nStudent removed successfully!")
        else:
            print("\nStudent not found.")

# Store students detail in a dictionary
student_dict = {
    1: Student(1, 'John', 'M', '20/02/2001', 4, 6, 'Bachelor', 'Phnom Penh', '016 921 128', 'John111@gmail.com'),
    2: Student(2, 'Wick', 'M', '14/07/2003', 2, 8, 'Bachelor', 'Phnom Penh', '011 727 990', 'Wicky121@gmail.com'),
    3: Student(3, 'Lisa', 'F', '09/03/2002', 3, 7, 'Bachelor', 'Phnom Penh', '097 985 3721', 'Slay101@gmail.com')
}

# Function to read Student.txt file and convert into a dictionary
def read_file():
    # Open file as read
    with open("Student.txt",'r') as file:
        # Divide and store information from the file to data
        data = file.read().rstrip("\n").split("\n")
        # Store information from data to a dictionary
        for item in data:
            stu = Student("", "", "", "", "", "", "", "", "", "")
            stu.id, stu.name, stu.gender, stu.dob, stu.year, stu.generation, stu.degree, stu.address, stu.phone_no, stu.email = item.split(", ")
            student_dict[int(stu.id)] = stu

# Function to display student information
def display_student(id):
    print("\n-------------------------------------------------------------------------------------------------------------------------------------------")
    print("ID   Name        Gender        DOB         Year     Generation     Degree       Address           PhoneNo.        Email")
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    print(str(id).ljust(4),
          student_dict[id].name.ljust(13),
          student_dict[id].gender.ljust(8),
          student_dict[id].dob.ljust(15),
          student_dict[id].year.ljust(11),
          student_dict[id].generation.ljust(9),
          student_dict[id].degree.ljust(13),
          student_dict[id].address.ljust(17),
          student_dict[id].phone_no.ljust(15),
          student_dict[id].email)
    
# Write students details from the dictionary to Student.txt file
def write_to_file():
    # Open file as write
    with open("Student.txt","w") as file:
        for key, student in student_dict.items():
            file.write(f'{key}, {student.name}, {student.gender}, {student.dob}, {student.year}, {student.generation}, {student.degree}, {student.address}, {student.phone_no}, {student.email}\n')

# Main
write_to_file()
while True:
    print("""\n
---------------------------
           MENU
---------------------------
a. Add New Student
b. Search Student by id
c. Update Student
d. Delete Student by id
e. Exit
    """)
    
    
    menu = input("Enter a menu: ").lower()
    # Create an object
    student = Student("", "", "", "", "", "", "", "", "", "")

    # Add a new student
    if(menu == 'a'):
        print("---------------------------")
        print("        Add Student        ")
        print("---------------------------")
        student.add_student()
        
    # Search for a student by id
    elif(menu == 'b'):
        print("---------------------------")
        print("       Search Student      ")
        print("---------------------------")
        id = int(input("Enter a student ID: "))
        student.search_student(id)

    # Update student information
    elif(menu == 'c'):
        print("---------------------------")
        print("      Update Student       ")
        print("---------------------------")
        student.update_student()

    # Delete a student
    elif(menu == 'd'):
        print("---------------------------")
        print("      Remove Student       ")
        print("---------------------------")
        id = int(input("Enter a student ID: "))
        student.delete_student(id)
    
    # Exit the program
    elif(menu == 'e'):
        exit(0)

    # print error if menu not from a to e
    else:
        print("Error! Please select menu from a to e")