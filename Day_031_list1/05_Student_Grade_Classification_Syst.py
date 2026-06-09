'''
5.Student Grade Classification System (Python List Assignment)

A school stores student marks in a list. The system must analyze the marks and generate a *clear performance report* 
by grouping students into grade categories.

Write a Python program to:

* Iterate through the list of marks
* Assign grades based on marks:

  * *>= 90 → A*
  * *>= 75 and < 90 → B*
  * *>= 50 and < 75 → C*
  * *< 50 → Fail*
* Store each category in separate lists
* Count students in each category
* Display a *final structured report (important)*

---
## 📌 Output Format (Mandatory)
Your output must be displayed exactly in this format:


===== STUDENT GRADE REPORT =====

A Grade Students   : [list]
B Grade Students   : [list]
C Grade Students   : [list]
Fail Students      : [list]

--------------------------------
A Count   : X
B Count   : X
C Count   : X
Fail Count: X
--------------------------------

Total Students: X

---
Input
[95, 82, 67, 45, 30]

Output

===== STUDENT GRADE REPORT =====

A Grade Students   : [95]
B Grade Students   : [82]
C Grade Students   : [67]
Fail Students      : [45, 30]

--------------------------------
A Count   : 1
B Count   : 1
C Count   : 1
Fail Count: 2
--------------------------------

Total Students: 5
'''

n = int(input('Enter the size of list: '))

print('Plz enter the marks...')

marks = []

i =0
while i < n:
   x = int(input('marks: '))
   marks.append(x)
   i += 1
print(marks)

print("===== STUDENT GRADE REPORT =====\n")
A = []
a_count = 0
for m in marks:
   if m >= 90:
      A.append(m)
      a_count += 1
print('A Grade Students   : ',A)

B = []
b_count = 0
for m in marks:
   if m >= 75 and m < 90:
      B.append(m)
      b_count += 1
print('B Grade Students   : ',B)


C = []
c_count = 0
for m in marks:
   if m >= 50 and m < 75:
      C.append(m)
      c_count += 1
print('C Grade Students   : ',C)


Fail = []
f_count = 0
for m in marks:
   if m < 50:
      Fail.append(m)
      f_count += 1
print('A Grade Students   : ',Fail, end="\n")


print('--------------------------------\n')
print("A Count    : ",a_count)
print("B Count    : ",b_count)
print("C Count    : ",c_count)
print("Fail Count : ",f_count,end="\n")
print('--------------------------------')

total = a_count + b_count + c_count + f_count 

print("Total Students: ", total)



