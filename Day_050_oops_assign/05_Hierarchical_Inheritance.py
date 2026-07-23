'''
ASSIGNMENT 5: School ERP System (Hierarchical Inheritance)
Scenario
A school is developing an ERP system.
Every person has common information.
Base Class
Person
Name
Age
Address
Derived Classes
Student
Roll Number
Course
Marks
Teacher
Employee ID
Subject
Salary
Principal
Office Number
Experience
Qualification
Functional Requirements
========== School ERP ==========
1. Add Student
2. Add Teacher
3. Add Principal
4. Display Student
5. Display Teacher
6. Display Principal
7. Exit
Sample Input
Choice : 1

Roll Number : 102
Name : Riya Sharma
Age : 20
Address : Indore

Course : Python Full Stack
Marks : 89
Sample Output
----------- Student Details -----------

Roll Number : 102
Name : Riya Sharma
Age : 20
Address : Indore

Course : Python Full Stack
Marks : 89

'''

class Person:

   def __init__(self, name, age, address):
  
       self.name = name
       self.age = age
       self.address = address

   def display(self):

       print("Name: ", self.name)
       print("Age: ", self.age)
       print("Address: ", self.address)

class Student(Person):

    def __init__(self, name, age, address, roll_no, course, marks):
        super().__init__(name, age, address)

        self.roll_no = roll_no
        self.course = course
        self.marks = marks

    def student_info(self):
       
        print("Roll No: ", self.roll_no)
        print("Course: ", self.course)
        print("Marks: ", self.marks) 
        
  
class Teacher(Person):

    def __init__(self, name, age, address, emp_id, sub, salary):
        super().__init__(name, age, address)
 
        self.emp_id = emp_id
        self.sub = sub
        self.salary = salary

    def teacher_info(self):
  
        print("Employee Id: ", self.emp_id)
        print("Subject: ", self.sub)
        print("Salary: ", self.salary)

class Principal(Person):

   def __init__(self, name, age, address, emp_id, salary, office_num, exp, qualification):

       super().__init__(name, age, address)
        
       self.emp_id = emp_id
       self.salary = salary
       self.office_num = office_num
       self.exp = exp
       self.qualification = qualification

   def principal_info(self):

       print("Employee ID:", self.emp_id)
       print("Salary:", self.salary)
 
       print("Office Number: ", self.office_num)
       print("Experience: ", self.exp)
       print("Qualification: ", self.qualification) 

student = None
teacher = None
principal = None

while True:

   print("\n========== School ERP ==========\n")
   print("1. Add Student")
   print("2. Add Teacher")
   print("3. Add Principal")
   print("4. Display Student")
   print("5. Display Teacher")
   print("6. Display Principal")
   print("7. Exit")

   choice = int(input("\nEnter choice: "))

   match choice:
      
      case 1:
            s_name = input("Enter Name: ")
            s_age = int(input("Enter Age: "))
            s_add = input("Enter Address: ")
            s_roll = int(input("Enter Roll Number: "))
            s_course = input("Enter Course Name: ")
            s_marks = int(input("Enter Marks: "))

            student = Student(s_name, s_age, s_add, s_roll, s_course, s_marks)

            print("Student added successfully....")


      case 2:
            t_name = input("Enter Name: ")
            t_age = int(input("Enter Age: "))
            t_add = input("Enter Address: ")
            t_id = int(input("Enter Employee ID: "))
            t_sub = input("Enter Subject Name: ")
            t_salary = int(input("Enter Salary: "))

            teacher = Teacher(t_name, t_age, t_add,  t_id, t_sub, t_salary)

            print("Teacher added successfully....")


      case 3:
            p_name = input("Enter Name: ")
            p_age = int(input("Enter Age: "))
            p_add = input("Enter Address: ")
            p_emp = int(input("Enter employee id"))
            p_salary = int(input("Enter salary: "))
            p_of_no = int(input("Enter Office Number: "))
            p_exp = input("Enter Experience: ")
            p_quali = input("Enter Qualification: ")

            principal = Principal(p_name, p_age, p_add, p_emp, p_salary, p_of_no, p_exp, p_quali)

            print("Principal added successfully....")

      case 4:
            if student:
               student.display()
               student.student_info()

            else:
               print("Student not available add firstly") 
 
      case 5:
            if teacher:
               teacher.display()
               teacher.teacher_info()

            else:
               print("Teacher not available add firstly") 

      case 6:
            if principal:
               principal.display()
               principal.principal_info()
  

            else:
               print("Principal not available add firstly") 

      case 7:
              print("Exit............")
              break 

 
