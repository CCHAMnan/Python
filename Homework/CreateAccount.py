# Create class
class Teacher:
    # Create constructor
    def __init__(self, id, name, gender, dob, address, phone_no, email):
        self.id = id
        self.name = name
        self.gender = gender
        self.dob = dob
        self.address = address
        self.phone_no = phone_no
        self.email = email

class Student:
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

# Parent class named Account
class Account:
    def __init__(self, id, username, password, phone_no, role=None):
        self.id = id
        self.username = username
        self.password = password
        self.phone_no = phone_no
        self.role = role
    
    # Create a method
    def create_account(self):
        id = int(input("Enter account ID: "))
        # check if id in account dictionary
        while id in account_dict:
            print("Account ID already exists! Please enter a new Account ID.")
            id = int(input("Enter account ID: "))

        username = input("Enter username: ")
        password = input("Enter password: ")
        phone_no = input("Enter phone number: ")
        # add all arguments to account constructor
        account = Account(id, username, password, phone_no)
        return account

# Create a child 
class TeacherAccount(Account):
    def __init__(self, id, username, password, phone_no, role, teacher_id):
        super().__init__(id, username, password, phone_no, role)
        self.role = "Teacher"
        self.teacher_id = teacher_id
    
    # create a method inside child class to overide the parent class
    def create_account(self):
        # call the read file function
        read_file("Teacher.txt")
        # use the method from the parent class(Account)
        account = super().create_account()
        teacher_id = int(input("Enter teacher ID: "))
        # check if teacher_id is in teacher dictionary or not
        while teacher_id not in teacher_dict:
            print("\nTeacher ID not found! Please Enter a new Teacher ID.")
            teacher_id = int(input("Enter teacher ID: "))
        
        # check if teacher_id already has an account
        if check_user_id(teacher_id) == True:
            print("\nTeacher ID already has an account!")
        else:
            # add all arguments to TeacherAccount constructor
            teacher = TeacherAccount(account.id, account.username, account.password, account.phone_no, self.role, teacher_id)
            account_dict[account.id] = teacher
            # call write_to_file function
            write_to_file()
            print("\nTeacher account created sucessfully!")

# Create a child 
class StudentAccount(Account):
    def __init__(self, id, username, password, phone_no, role, student_id):
        super().__init__(id, username, password, phone_no, role)
        self.role = "Student"
        self.student_id = student_id

    # create a method inside child class to overide the parent class
    def create_account(self):
        read_file("Student.txt")
        # use the method from the parent class(Account)
        account = super().create_account()
        student_id = int(input("Enter student ID: "))
        # check if student_id is in student dictionary or not
        while student_id not in student_dict:
            print("\nStudent ID not found! Please Enter a new Student ID.")
            student_id = int(input("Enter student ID: "))

        # check if student_id already has an account
        if check_user_id(student_id) == True:
            print("\nStudent ID already has an account!")
        else:
            # add all arguments to StudentAccount constructor
            student = StudentAccount(account.id, account.username, account.password, account.phone_no, self.role, student_id)
            account_dict[account.id] = student
            write_to_file()
            print("\nStudent account created sucessfully!")

teacher_dict = {
    1: Teacher(1, 'Albert', 'M', '01/04/1960', 'Ta Kmav', '012 212 121', 'Albert120@gmail.com'),
    2: Teacher(2, 'Einstein', 'M', '18/04/1955', 'Chom Chao', '012 212 121', 'Albert120@gmail.com'),
    3: Teacher(3, 'Newton', 'M', '17/01/1980', 'Steung Mean Chey', '012 212 121', 'Albert120@gmail.com')
}

student_dict = {
    1: Student(1, 'John', 'M', '20/02/2001', 4, 6, 'Bachelor', 'Phnom Penh', '016 921 128', 'John111@gmail.com'),
    2: Student(2, 'Wick', 'M', '14/07/2003', 2, 8, 'Bachelor', 'Phnom Penh', '011 727 990', 'Wicky121@gmail.com'),
    3: Student(3, 'Lisa', 'F', '09/03/2002', 3, 7, 'Bachelor', 'Phnom Penh', '097 985 3721', 'Slay101@gmail.com')
}

account_dict = {
    1: TeacherAccount(1, 'Jack', 'pass2023', '016 921 128', 'Teacher', 1),
    2: StudentAccount(2, 'DarkSoul', 'Nogamenolife', '011 727 990', 'Student', 1),
    3: StudentAccount(3, 'Lily', 'Onlyyou<3', '097 985 3721', 'Student', 2)
}

# function to check if userID already has an account or not
def check_user_id(id):
    for userID in account_dict.values():
        if isinstance(userID, TeacherAccount) and userID.teacher_id == id:
            return True
        elif isinstance(userID, StudentAccount) and userID.student_id == id:
            return True
        return False

# Write information from dictionary into a file
def write_to_file():
    # Open file Account.txt as write
    with open("Account.txt",'w') as file:
        for key, account in account_dict.items():
            # check if the object belong to a specific class
            if isinstance(account, TeacherAccount):
                file.write(f'{key}, {account.username}, {account.password}, {account.phone_no}, {account.role}, {account.teacher_id}\n')
            elif isinstance(account, StudentAccount):
                file.write(f'{key}, {account.username}, {account.password}, {account.phone_no}, {account.role}, {account.student_id}\n')
    
    # Open file Student.txt as write
    with open("Student.txt",'w') as file:
        for key, student in student_dict.items():
            file.write(f'{key}, {student.name}, {student.gender}, {student.dob}, {student.year}, {student.generation}, {student.degree}, {student.address}, {student.phone_no}, {student.email}\n')

    # Open file Teacher.txt as write
    with open("Teacher.txt",'w') as file:
        for key, teacher in teacher_dict.items():
            file.write(f'{key}, {teacher.name}, {teacher.gender}, {teacher.dob}, {teacher.address}, {teacher.phone_no}, {teacher.email}\n')

# Function to read file and convert it into a dictionary
def read_file(filename):
    # Open file as read
    with open(filename,'r') as file:
        # Divide and store information from a dictionary to data
        data = file.read().rstrip("\n").split("\n")
        # Store information from data into a dictionary
        for item in data:
            if filename == "Student.txt":
                stu = Student("", "", "", "", "", "", "", "", "", "")
                stu.id, stu.name, stu.gender, stu.dob, stu.year, stu.generation, stu.degree, stu.address, stu.phone_no, stu.email = item.split(", ")
                student_dict[int(stu.id)] = stu
            elif filename == "Teacher.txt":
                teach = Teacher("", "", "", "", "", "", "")
                teach.id, teach.name, teach.gender, teach.dob, teach.address, teach.phone_no, teach.email = item.split(", ")
                teacher_dict[int(teach.id)] = teach

# Main
write_to_file()
while True:
    print("""\n
---------------------------
           MENU
---------------------------
a. Create Teacher Account
b. Create Student Account
c. Exit
    """)

    menu = input("Enter a menu: ").lower()
    teacher = TeacherAccount("", "", "", "", "", "")
    student = StudentAccount("", "", "", "", "", "")

    # Create Teacher Account
    if(menu == 'a'):
        print("---------------------------")
        print("      Teacher Account      ")
        print("---------------------------")
        teacher.create_account()
        
    # Create Student Account
    elif(menu == 'b'):
        print("---------------------------")
        print("      Student Account      ")
        print("---------------------------")
        student.create_account()

    # Exit the program
    elif(menu == 'c'):
        exit(0)

    # print error if menu not from a to c
    else:
        print("Error! Please select menu from a to c")
