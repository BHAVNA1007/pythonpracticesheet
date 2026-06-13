'''2.

ASSIGNMENT: ONLINE COURSE ENROLLMENT & STUDENT MANAGEMENT SYSTEM

A training institute offers multiple courses such as Python, Java, Full Stack Development, Data Science, and React.

Currently, student enrollment details are maintained manually in Excel sheets. As the number of students is increasing, the institute wants to develop a Student Management System using Python.

The system should store student records in a nested dictionary where:

Key → Student ID
Value → Dictionary containing student information

Each student record should contain:
Student Name
Course Name
Mobile Number
Fees
City
Sample Data Structure
{
101:{
    "name":"Ajay",
    "course":"Python",
    "mobile":"9876543210",
    "fees":25000,
    "city":"Indore"
},
102:{
    "name":"Ravi",
    "course":"Java",
    "mobile":"9876500000",
    "fees":22000,
    "city":"Bhopal"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=========================================
 STUDENT MANAGEMENT SYSTEM
=========================================

1. Add New Student
2. Search Student
3. Update Course
4. Delete Student
5. Display All Students
6. Count Total Students
7. Display Students By Course
8. Display Students By City
9. Find Student Paying Highest Fees
10. Find Student Paying Lowest Fees
11. Exit
Functional Requirements
1. Add New Student

Accept the following details:

Student ID
Student Name
Course Name
Mobile Number
Fees
City

Store the information in the nested dictionary.

Validation

If Student ID already exists:

Student ID Already Exists
2. Search Student

Accept Student ID from the user.

If found, display complete student information.

Sample Output
Student ID : 101
Name       : Ajay
Course     : Python
Mobile     : 9876543210
Fees       : 25000
City       : Indore

If not found:

Student Not Found
3. Update Course

Accept Student ID.

If found:

Ask for new course name.
Update the course.
Sample Output
Course Updated Successfully
4. Delete Student

Accept Student ID.

If found:

Delete the record.
Sample Output
Student Deleted Successfully

Otherwise:

Student Not Found
5. Display All Students

Display all student records in a proper format.

Sample Output
-----------------------------------
Student ID : 101
Name       : Ajay
Course     : Python
Fees       : 25000
-----------------------------------

Student ID : 102
Name       : Ravi
Course     : Java
Fees       : 22000
-----------------------------------
6. Count Total Students

Display total number of students enrolled.

Sample Output
Total Students : 45
7. Display Students By Course

Accept a course name from the user.

Display all students enrolled in that course.

Sample Output
Enter Course : Python

101  Ajay
105  Neha
112  Aman

If no students are found:

No Students Found
8. Display Students By City

Accept city name from the user.

Display all students belonging to that city.

Sample Output
Enter City : Indore

101  Ajay
108  Ravi
115  Pooja
9. Find Student Paying Highest Fees

Display complete details of the student who has paid the highest fees.

Sample Output
Highest Fee Paying Student

Student ID : 121
Name       : Neha
Course     : Data Science
Fees       : 50000
10. Find Student Paying Lowest Fees

Display complete details of the student who has paid the lowest fees.

Sample Output
Lowest Fee Paying Student

Student ID : 131
Name       : Aman
Course     : React
Fees       : 15000
11. Exit

Terminate the application.

Sample Output
Thank You For Using Student Management System
'''


n = int(input("Enter num of Student: "))
Student = {}

for i in range(n):
    s_id = int(input("Student ID: "))
   
    name = input("name: ")
    course = input("Course: ")
    mobile_n = input("Mobile Number: ")
    fees = int(input("Fees: "))
    city = input("City: ")
    Student[s_id]    = {
       "name": name,
       "course": course,
       "mobile_n":  mobile_n,
       "fees":  fees,
       "city": city
    }
#print(Student)

while True:
    print("ONLINE COURSE ENROLLMENT & STUDENT MANAGEMENT SYSTEM")
    print("1. Add New Student")
    print("2. Search Student")
    print("3. Update Course")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Count Total Students")
    print("7. Display Students By Course")
    print("8. Display Students By City")
    print("9. Find Student Paying Highest Fees")
    print("10. Find Student Paying Lowest Fees") 
    print("11. Exit")
    
    choice = int(input("Enter choice: "))
    
    match choice:
        case 1:
            s_id = int(input("Student_ID: "))
            if s_id in Student:
                print("Student_ID already exists.")
            else:
                name = input("name: ")
                course = input("course: ")
                mobile_n = input("mobile_n: ")
                fees = int(input("fees: "))
                city = input("city: ")
                Student[s_id]    = {
                     "name": name,
                     "course": course,
                     "mobile_n":  mobile_n,
                     "fees": fees,
                     "city": city
                }
                print("New Student added successfully:  ",Student)  
        case 2:
            s_id = int(input("Enter id: "))
            if s_id in Student:
                print(" Student found successfully:  ") 
                print("s_id: ", s_id)    
                for k, v in Student[s_id].items():
                    print(k, ":", v)
                
            else:    
                print("Student Record Not Found:  ")      
                
        case 3:
            s_id = int(input("Enter Student id: "))
            if s_id in Student:
                n_c = input(" enter  new Course:  ")    
                Student[s_id]["course"] = n_c
                print("course updated successfully: ",)
                print("s_id: ", s_id)    
                for k, v in Student[s_id].items():
                    print(k, ":", v)
            else:    
                print("Student Record Not Found:  ")      

        case 4:
            s_id = int(input("Enter id: "))
            if s_id in Student:
                
                del Student[s_id]
                print("Student Record deleted successfully: ",)
                print(Student)  
            else:    
                print("Student Record Not Found:  ")            
        

        case 5:
            print("All Student Records")

            for s_id, details in Student.items():
                print("--------------------------")
                print("Student ID:", s_id)

                for k, v in details.items():
                    print(f"{k}: {v}")

            print("--------------------------")  
        case 6:
            print("All  Student Count: ")
            count = 0 
            for s_id, details in  Student.items():
                count += 1
            print(" Student count = ", count)  
                
        case 7:
            print("Display Students By Course")
            course = input("Enter Course: ")
            f = False
            for s_id, s in Student.items():
                if    s["course"] == course:
                    f = True    
                    print(s_id, s["name"])    
                
            if not f:    
                print("Student Record Not Found:  ")      
                
        case 8:
            print(" Display Students By City")
            city = input("Enter City: ")
            f = False
            for s_id, c in Student.items():
                if    c["city"] == city:
                    f = True    
                    print(s_id, c["name"])    
                
            if not f:    
                print("Student Record Not Found:  ")      
                        
        case 9:
            print("9. Find Student Paying Highest Fees")
            h_pay = 0
            h_id =None
   
            for s_id, h in Student.items():
                if h["fees"]> h_pay:
                    h_pay = h["fees"]
                    h_id = s_id
            print("Student Paying Highest Fees: ")
            print("Student  Id: ", h_id)
            
            for k, v in Student[h_id].items():
                print(k,":",v)
                
        case 10:
            print("10. Find Student Paying Lowest Fees")
            l_pay = float('inf')
            l_id =None
   
            for s_id, l in Student.items():
                if l["fees"]< l_pay:
                    l_pay = l["fees"]
                    l_id = s_id
            print("Student Paying Lowest Fees: ")
            print("Student Id: ", l_id)
            
            for k, v in Student[l_id].items():
                print(k,":",v)
              
        case 11:
            print("Thank You For Using Student Management System")
            break       
            


