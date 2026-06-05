'''
QUESTION 2: STUDENT RESULT PROCESSING
=====================================

A training institute wants to manage student records using NamedTuple.

Fields:
roll_no, name, course, marks

Requirements:

1. Read N student records from the user and store them in a list of NamedTuples.

---

2. Display all student details.

---

3. Find and display the topper of the class.

---

4. Count and display the number of students scoring above 80 marks.

---

5. Calculate and display the average marks.

---

6. Accept a course name from the user and display all students enrolled in that course.

---

Test Case:

Input:
Enter number of students: 4

1 Ravi Python 85
2 Anjali Java 78
3 Karan Python 92
4 Pooja Testing 88

Enter course: Python

Expected Output:
Topper:
3 Karan Python 92

Students Above 80:
3

Average Marks:
85.75

Students in Python Course:
1 Ravi Python 85
3 Karan Python 92
'''

from collections import namedtuple

n = int(input("Enter no of students:  "))

students = namedtuple("students",['roll_no', 'name', 'course', 'marks'])

Namedtuples = []

for i in range(n):
   print(f"Enter student{i+1} details:")
   r = int(input("Enter student roll no: "))
   name = input("Enter student name: ")
   c = input("Enter  course: ")
   m = float(input("Enter marks: "))
   Namedtuples.append(students(r,name,c,m))



for student in Namedtuples:
    print(student.roll_no,end=' ')
    print(student.name,end=' ')
    print(student.course,end=' ')
    print(student.marks,end=' ')
    print()

       
topper = Namedtuples[0]
for student in Namedtuples:

    if  topper.marks < student.marks:
        topper = student
         

print("\nEmployee with Highest Salary: ")
print(topper.roll_no,end=' ')
print(topper.name,end=' ')
print(topper.course,end=' ')
print(topper.marks,end=' ')
print()


count = 0
for student in Namedtuples:

    if  student.marks > 80:
        count += 1
         
print("\nStudents Above 80: ",count)
print()

count = 0
sum = 0
for student in Namedtuples:
   count += 1
   sum += student.marks
   avg = sum / count

print("\nAverage marks", avg)



print("\nStudents in Python Course: ")   
dep = input("\nEnter Course: ") 
  
for student in Namedtuples:
   
   if student.course == "Python":
       print(student.roll_no,end=' ')
       print(student.name,end=' ')
       print(student.course,end=' ')
       print(student.marks,end=' ')
       print()


