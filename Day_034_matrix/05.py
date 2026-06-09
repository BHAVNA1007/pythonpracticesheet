'''
5.
=============================================================
 Student Classroom Matrix Analysis
=============================================================

Scenario

A school stores student marks in a matrix.

Rows represent different classrooms.
Columns represent students in each classroom.

The principal wants to analyze the performance of each classroom by
calculating the total marks scored by students in every row.

Requirements

* Read number of rows from user
* Read number of columns from user
* Read all matrix elements from user
* Display the complete matrix
* Find Row Wise Sum
* Display sum of each row separately

Test Case 1

Input:

Rows = 3
Columns = 3

Matrix:

10 20 30
40 50 60
70 80 90

Output:

Matrix:

10 20 30
40 50 60
70 80 90

Row 1 Sum = 60
Row 2 Sum = 150
Row 3 Sum = 240

------------------------------------------------------------

Test Case 2

Input:

Rows = 2
Columns = 4

Matrix:

1 2 3 4
5 6 7 8

Output:

Matrix:

1 2 3 4
5 6 7 8

Row 1 Sum = 10
Row 2 Sum = 26

------------------------------------------------------------

Test Case 3

Input:

Rows = 2
Columns = 2

Matrix:

100 200
300 400

Output:

Matrix:

100 200
300 400

Row 1 Sum = 300
Row 2 Sum = 700

------------------------------------------------------------

Additional Challenge

Also Display:

* Row Wise Sum
* Row Wise Average
* Row Having Maximum Sum
* Grand Total of Matrix

Sample Output

===== MATRIX REPORT =====

Matrix:

10 20 30
40 50 60
70 80 90

Row 1 Sum = 60
Row 2 Sum = 150
Row 3 Sum = 240

Row 1 Average = 20.0
Row 2 Average = 50.0
Row 3 Average = 80.0

Maximum Sum Row = Row 3
Grand Total = 450

========================================================
'''
rows = int(input("Rows: "))
cols = int(input("Columns: "))

matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)

print("===== MATRIX REPORT =====\n ")
print("Matrix:\n") 

for i in range(len(matrix)):
   for j in range(len(matrix[i])):
        print(matrix[i][j],end=" ") 
       
   print()
print()
    

g_total = 0
m_sum = 0
m_row = 0

for i in range(len(matrix)):
   total = 0
   
   for j in range(len(matrix[i])):
       total += matrix[i][j]
       g_total += matrix[i][j]

   print(f"Row {i+1} Sum = {total}") 

   if total > m_sum:
      m_sum = total
      m_row = i + 1

print()


for i in range(len(matrix)):
   total = 0
   count = 0
   for j in range(len(matrix[i])):
       total += matrix[i][j]
       count += 1
       avg = total /count

   print(f"Row {i+1} Average = {avg }") 
print()

print("Grand Total = ",g_total)
print("Maximum Sum Row = ","Row",m_row)



    



    


