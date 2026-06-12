'''
4.
=========================================
STUDENT GRADE ANALYSIS
======================

Store student marks in a dictionary.

students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}

Write a program to:

* Find the student with highest marks.
* Find the student with lowest marks.

Sample Output:
Highest Marks : Ravi 92
Lowest Marks : Aman 65
'''

n = int(input("Enter num of student: "))

students = {}
for i in range(n):
    key = input("Name: ")
    value = int(input("marks: "))
    students[key] = value
print(students)    

h_m = -1
h_name = ""

l_m = float("inf")
l_name = ""
for k, v in students.items():
    if v  >  h_m:
            h_m = v
            h_name = k
            
    if v  <  l_m:
            l_m = v
            l_name = k
            
print("Highest Marks :", h_m)    
print("Lowest Marks : ", l_m)         
                    
            