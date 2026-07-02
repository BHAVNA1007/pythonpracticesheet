'''
Question 4: Student Result Processing System
Scenario

A college wants to automate result generation by calculating total marks, percentage, and grade.

Requirements

Create a class named Student with:

roll_number
student_name
marks1
marks2
marks3

Initialize the values using a constructor.

Calculations
Total = Marks1 + Marks2 + Marks3
Percentage = Total / 3
Grade Criteria
Percentage	Grade
90 and above	A
75 to 89	B
60 to 74	C
Below 60	D
Sample Input
Enter Roll Number : 101
Enter Student Name : Priya Sharma
Enter Marks in Subject 1 : 85
Enter Marks in Subject 2 : 90
Enter Marks in Subject 3 : 88
Sample Output
------ Student Result ------
Roll Number      : 101
Student Name     : Priya Sharma
Total Marks      : 263
Percentage       : 87.67
Grade            : B
'''

class Student:

     def __init__(self, roll_number, student_name, marks1, marks2, marks3):

         self.roll_num = roll_number
         self.s_name = student_name
         self.m1 = marks1
         self.m2 = marks2
         self.m3 = marks3

         self.total = self.m1 + self.m2 + self.m3

         self.per =  self.total / 3

         if self.per >= 90:
            self.grade = "A"

         elif self.per < 90 and self.per >= 75: 
             self.grade = "B"

         elif self.per < 75 and self.per >= 60: 
             self.grade = "C"

         elif self.per < 60: 
             self.grade = "B"

def main():

     roll_number = int(input("Enter Roll Number :"))
     student_name = input("Enter Student Name :")
     marks1 = int(input("Enter Marks in Subject 1 :"))
     marks2 = int(input("Enter Marks in Subject 2 :"))
     marks3 = int(input("Enter Marks in Subject 3 :"))

     s = Student(roll_number, student_name, marks1, marks2, marks3)

     print("\n------ Student Result ------\n")
     
     print("\nRoll Number      : ", s.roll_num)
     print("Student Name     : ", s.s_name)
     print("Total Marks      : ", s.total)
     print("Percentage       : ", s.per)
     print("Grade            : ", s.grade)

main()




 


        
 

      