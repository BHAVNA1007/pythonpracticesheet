'''
4.
=========================================================
        MATRIX DIAGONAL ANALYSIS SYSTEM
=========================================================

Scenario

A security company stores surveillance data in matrix form.
The analyst wants a menu-driven application to examine the
diagonal elements of the matrix and generate reports.

The application should allow the user to:

1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Display Main Diagonal Elements
   2. Display Secondary Diagonal Elements
   3. Compare Main and Secondary Diagonal Sums
   4. Exit

2. Read the size of a square matrix from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Display Main Diagonal Elements
   -----------------------------------------
   Display all elements present in the main diagonal.

5. Choice 2 - Display Secondary Diagonal Elements
   ----------------------------------------------
   Display all elements present in the secondary diagonal.

6. Choice 3 - Compare Main and Secondary Diagonal Sums
   ---------------------------------------------------
   Calculate the sum of both diagonals and display:

   - Main Diagonal Sum
   - Secondary Diagonal Sum
   - Which diagonal has the greater sum
   - Or whether both sums are equal

7. Choice 4 - Exit
   -----------------------------------------
   Display:
   "Thank You for Using Matrix Diagonal Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Enter size of matrix: 3

Enter matrix elements:

1 2 3
4 5 6
7 8 9

Menu
1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

Enter your choice: 1

Output:
Main Diagonal Elements:
1 5 9

---------------------------------------------------------

Enter your choice: 2

Output:
Secondary Diagonal Elements:
3 5 7

---------------------------------------------------------

Enter your choice: 3

Output:
Main Diagonal Sum = 15
Secondary Diagonal Sum = 15
Both Diagonal Sums are Equal

=========================================================
'''

r = int(input("Rows: "))
c = int(input("Columns: "))

print("ele for m1...")
matrix = []
for i in range(r):
   row = []
   for j in range(c):
       row.append(int(input()))
   matrix.append(row)
print()

print("\nMatrix1: ")
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=' ')
    print()
print()

while  True:
   print("==MENU==")
   print("1. Display Main Diagonal Elements")
   print("2. Display Secondary Diagonal Elements")
   print("3. Compare Main and Secondary Diagonal Sums")
   print("4. Exit")
    
   choice = int(input("Enter your choice: "))
   match choice: 
         case 1:
             print("Main Diagonal Elements are :")
             for i in range(len(matrix)):
                
                for j in range(len(matrix[i])):
                   dia = matrix[i][i]

                print(dia,end=' ')  
             print()

         case 2:
             print("Secondary  Diagonal Elements are :")
             n = len(matrix)
                
             for i in range(n):
                   print(matrix[i][n-1-i],end=" ")

                 
             print()
         case 3:
             sum = 0
             for i in range(len(matrix)):
                   sum += matrix[i][i]
                   
             print(sum)  
             print()

         case 4:
             print("Thank You for Using Matrix Operations")

             break


              
           
