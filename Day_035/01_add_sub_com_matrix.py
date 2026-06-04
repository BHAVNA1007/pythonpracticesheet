'''
1.
=========================================================
        MATRIX OPERATIONS MANAGEMENT SYSTEM
=========================================================


A data analysis company stores numerical information in matrix form.
To help employees perform matrix-related operations efficiently,
the company wants a menu-driven application.

The application should allow the user to:

1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

The user must enter the number of rows, columns, and all matrix
elements. The program should perform the selected operation and
display the result.

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user chooses Exit.

   1. Add Two Matrices
   2. Subtract Two Matrices
   3. Compare Two Matrices
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all elements of Matrix A and Matrix B from the user whenever
   required.

4. Based on the user's choice:

   Choice 1 - Add Two Matrices
   --------------------------------
   Add corresponding elements of both matrices and display
   the resultant matrix.

5. Choice 2 - Subtract Two Matrices
   --------------------------------
   Subtract corresponding elements of Matrix B from Matrix A
   and display the resultant matrix.

6. Choice 3 - Compare Two Matrices
   --------------------------------
   Check whether both matrices are equal.

   Two matrices are considered equal if:
   - They have the same dimensions.
   - Corresponding elements are equal.

   Display:
   "Matrices are Equal"
   or
   "Matrices are Not Equal"

7. Choice 4 - Exit
   --------------------------------
   Display:
   "Thank You for Using Matrix Operations Management System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 1

Enter number of rows: 2
Enter number of columns: 2

Enter Matrix A:
1 2
3 4

Enter Matrix B:
5 6
7 8

Result Matrix:
6 8
10 12

---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 3

Enter number of rows: 2
Enter number of columns: 2

Enter Matrix A:
1 2
3 4

Enter Matrix B:
1 2
3 4

Output:
Matrices are Equal

---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 4

Output:
Thank You for Using Matrix Operations Management System

=========================================================
'''

while  True:
  
    print("==MENU==")
    print("1. Add Two Matrices")
    print("2. Subtract Two Matrices")
    print("3. Compare Two Matrices")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    match choice: 

          case 1:
            r = int(input("Rows: "))
            c = int(input("Columns: "))

            print("ele for m1...")
            matrix1 = []

            for i in range(r):
                row = []
                for j in range(c):
                   row.append(int(input()))
                matrix1.append(row)
            print()

            print("ele for m2...")
            matrix2 = []
 
            for i in range(r):
                row = []
                for j in range(c):
                   row.append(int(input()))
                matrix2.append(row)
            print()


            print("\nMatrix1: ")
            for i in range(r):
                for j in range(c):
                   print(matrix1[i][j],end=' ')
                print() 

            print("\nMatrix2: ")
            for i in range(r):
                for j in range(c):
                    print(matrix2[i][j],end=' ')
                print() 
      
            
            m3 = []
            for i in range(r):
                row = []
                for j in range(c):
                    row.append(matrix1[i][j]+matrix2[i][j])
                m3.append(row)

            print("\nM3 sum of two matrix: ")
            for i in range(r):
                for j in range(c):
                    print(m3[i][j],end=' ')
                print() 
           
          case 2:
                r = int(input("Rows: "))
                c = int(input("Columns: "))

                print("ele for m1...")
                matrix1 = []

                for i in range(r):
                   row = []
                   for j in range(c):
                      row.append(int(input()))
                   matrix1.append(row)
                print()

                print("ele for m2...")
                matrix2 = []
 
                for i in range(r):
                   row = []
                   for j in range(c):
                      row.append(int(input()))
                   matrix2.append(row)
                print()


                print("\nMatrix1: ")
                for i in range(r):
                    for j in range(c):
                         print(matrix1[i][j],end=' ')
                    print() 

                print("\nMatrix2: ")
                for i in range(r):
                    for j in range(c):
                       print(matrix2[i][j],end=' ')
                    print() 
      
            
                m3 = []
                for i in range(r):
                   row = []
                   for j in range(c):
                      row.append(matrix1[i][j]-matrix2[i][j])
                   m3.append(row)
    
                print("\nM3 subtraction of two matrix: ")
                for i in range(r):
                   for j in range(c):
                      print(m3[i][j],end=' ')
                   print() 
         
          case 3:
                r = int(input("Rows: "))
                c = int(input("Columns: "))

                print("ele for m1...")
                matrix1 = []

                for i in range(r):
                   row = []
                   for j in range(c):
                      row.append(int(input()))
                   matrix1.append(row)
                print()

                print("ele for m2...")
                matrix2 = []
 
                for i in range(r):
                   row = []
                   for j in range(c):
                      row.append(int(input()))
                   matrix2.append(row)
                print()


                print("\nMatrix1: ")
                for i in range(r):
                    for j in range(c):
                         print(matrix1[i][j],end=' ')
                    print() 

                print("\nMatrix2: ")
                for i in range(r):
                    for j in range(c):
                       print(matrix2[i][j],end=' ')
                    print() 
      
            
           
                print("\nM3 comparision of two matrix: ")
                equal = 1
                for i in range(r):
                   for j in range(c):
                       if matrix1[i][j] != matrix2[i][j] :
                           equal = 0
                           break 
                   if equal==0:
                      break
                  
                if equal==1:
                    print("Matrices are Equal")  
                else:
                    print("Matrices are not Equal")

          case 4:
                print('''Thank You for Using Matrix Operations    
                Management System''')

                break
                    
           

    

            
                                        
   





 


