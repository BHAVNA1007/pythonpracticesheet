'''
1.STUDENT RESULT MANAGEMENT SYSTEM

Scenario:

A college examination department wants to automate the process of generating student results. The staff should be able to enter student details, calculate marks, determine grades, and display a complete report card using a menu-driven application.

Develop a Python program using multiple user-defined functions and a menu-driven approach to perform the following operations.

MENU

1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Complete Result
6. Find Highest Subject Mark
7. Find Lowest Subject Mark
8. Exit

Functional Requirements

1. Add Student Details

   * Student Name
   * Roll Number
   * Marks of 5 Subjects

2. Calculate Total Marks

3. Calculate Percentage

4. Find Grade

5. Display Complete Result

6. Find Highest Subject Mark

7. Find Lowest Subject Mark

8. Exit

Grade Criteria

Percentage        Grade

90 - 100          A+
80 - 89           A
70 - 79           B
60 - 69           C
50 - 59           D
Below 50          Fail

Constraints

* Marks should be between 0 and 100.
* Display an appropriate message for invalid marks.
* The program should continue until the user chooses Exit.

Sample Input / Output

*** STUDENT RESULT MANAGEMENT ***

1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Result
6. Find Highest Mark
7. Find Lowest Mark
8. Exit

Enter Choice : 1

Enter Student Name : Ajay
Enter Roll Number : 101

Enter Mark 1 : 78
Enter Mark 2 : 85
Enter Mark 3 : 92
Enter Mark 4 : 88
Enter Mark 5 : 77

Student details added successfully.

Enter Choice : 2

Total Marks = 420

Enter Choice : 3

Percentage = 84.0

Enter Choice : 4

Grade = A

Enter Choice : 6

Highest Mark = 92

Enter Choice : 7

Lowest Mark = 77

Enter Choice : 5

----------- RESULT CARD -----------

Name        : Ajay
Roll Number : 101

Marks
Subject 1 : 78
Subject 2 : 85
Subject 3 : 92
Subject 4 : 88
Subject 5 : 77

Total Marks : 420
Percentage  : 84.0
Grade       : A
Highest Mark: 92
Lowest Mark : 77

Enter Choice : 8

Thank You. Program Terminated.

Important Instructions

1. The solution must be developed using multiple user-defined functions.
2. Use appropriate parameters wherever data needs to be passed between functions.
3. Use return statements wherever a function needs to send a result back to the caller.
4. Avoid using unnecessary global variables.
5. Implement the application using a menu-driven approach.
6. Perform proper input validation.
7. Write meaningful function names and maintain proper code readability.

'''

def Student_Details():
    name = input("Enter Student Name :")
    roll_n = int(input("Enter Roll Number :"))
    
    n = int(input("Marks:"))
    marks = []
    for m in range(n):
        
        mark = int(input(f"Enter Mark {m+1} :")) 

        while mark<0 or mark>100:
            print("Invalid marks")
            mark = int(input(f"Enter Mark {m+1} :")) 
        marks.append(mark)
         
    print("Student details added successfully.")

    return name, roll_n, marks

def cal_marks(marks):
   total = 0
   for m in marks:
       total += m 
   return total

def percentage(marks):
   
    total = cal_marks(marks)
  
    return (total/500)*100

def grade(marks):

    g = percentage(marks)

    if  90 <= g <= 100:
       return "A+"

    elif 80 <= g < 90:
       return "A"

    elif 70 <= g < 80:
       return "B"

    elif 60 <= g < 70:
       return "C"

    elif 50 <= g < 60:
       return "D"

    else:
       return "Fail" 

def highest_mark(marks):
    h_m = marks[0]
    for m in marks:
        if m > h_m:
           h_m = m
    return h_m 

def lowest_mark(marks):
    l_m = marks[0]
    for m in marks:
        if m < l_m:
           l_m = m
    return l_m 
              

def main():

   name = ""
   roll_n = 0
   marks = []

   print("*** STUDENT RESULT MANAGEMENT ***\n\n")
   print("1. Add Student Details")
   print("2. Calculate Total Marks")
   print("3. Calculate Percentage")
   print("4. Find Grade")
   print("5. Display Result")
   print("6. Find Highest Mark")
   print("7. Find Lowest Mark")
   print("8. Exit")

   while True:
       choice = int(input("Enter choice: "))

       match choice:
             case 1:
                  print("\n1. Add Student Details") 
                  name, roll_n, marks = Student_Details()
                 
             case 2:
                  print("\n2. Calculate Total Marks")
                  
                  if marks:
                     total = cal_marks(marks)
                     print("Total marks: ",total)
                  else:
                     print("Please add stu details first") 
             case 3:
                  print("\n3. Calculate Percentage")

                  if marks:
                     res = percentage(marks)
                     print("Percentage: ",res)

             case 4:
                  print("\n4. Find Grade")

                  if marks:
                      g = grade(marks)
                      print("Grade =", g) 
             
             case 6:
                  print("\n6. Find Highest Mark")

                  if marks:
                      highest = highest_mark(marks)
                      print("highest mark: ",highest)

             case 7:
                  print("\n7. Find Lowest Mark")
                  
                  if marks:
                     lowest = lowest_mark(marks)
                     print("Lowest Mark: ",lowest) 
  
             case 5:
                  print("\n5. Display Result")

                  print("----------- RESULT CARD -----------")
                  if marks:
                      total = cal_marks(marks)
                      res = percentage(marks)
                      g = grade(marks)
                      lowest = lowest_mark(marks)

                      print("\nname  :", name)
                      print("Roll No : ", roll_n)
                      print("\nMarks")


                      for i in range(len(marks)):
                          print(f"Mark {i+1} :  {marks[i]} ") 
    
                      
                      print("\nTotal marks: ",total)
                      print("Percentage: ",res)
                      print("Grade :", g)
                      print("highest mark: ",highest)
                      print("Lowest Mark: ",lowest) 


             case 8:
                  print("Thank You. Program Terminated.")
                  break  
main()
                   











    
   
    
    



