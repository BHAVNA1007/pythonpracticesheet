'''7.
=========================================
ONLINE EXAM RESULT SYSTEM
=========================

Store student marks in a dictionary.

results = {
"Ajay":88,
"Ravi":45,
"Neha":76,
"Aman":39
}

Write a program to:

* Display names of students who passed.
  (Passing Marks = 50)

Sample Output:
Ajay
Neha
Ravi
'''
n = int(input("Enter num of student: "))

students = {}
for i in range(n):
    key = input("Name: ")
    value = int(input("marks: "))
    students[key] = value
print(students)    

for k, v in students.items():
    if v >= 50:
        print(k) 