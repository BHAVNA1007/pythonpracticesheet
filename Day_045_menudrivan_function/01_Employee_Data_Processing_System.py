'''
Employee Data Processing System

A company stores information about its employees in two forms:

A list of employee ages.
A string containing employee names separated by spaces.

The HR department wants a Python application that can perform different operations on this data through a menu-driven system. To make the application modular and easy to maintain, each operation must be implemented using a separate function that accepts data as a parameter and returns the result.

Problem Statement

Develop a menu-driven Python application called Employee Data Processing System.

The program should allow the HR department to perform the following operations:

Functions on Employee Ages (List)
1. find_second_highest_age(age_list)
Accept a list of employee ages.
Return the second highest age.
2. count_senior_employees(age_list)
Accept a list of employee ages.
Consider employees aged 50 years or above as senior employees.
Return the count of senior employees.
3. remove_duplicate_ages(age_list)
Accept a list of employee ages.
Return a new list after removing duplicate ages while maintaining the original order.
Functions on Employee Names (String)
4. count_names_starting_with_vowel(names)
Accept a string containing employee names separated by spaces.
Return the number of names that start with a vowel (A, E, I, O, U).
5. longest_name(names)
Accept a string containing employee names separated by spaces.
Return the employee name having the maximum number of characters.
Menu
========== EMPLOYEE DATA PROCESSING SYSTEM ==========
1. Find Second Highest Employee Age
2. Count Senior Employees
3. Remove Duplicate Ages
4. Count Names Starting with a Vowel
5. Find Longest Employee Name
6. Exit
====================================================
Enter your choice:
Sample Input
Employee Ages:
34 55 29 60 55 42 60 51

Employee Names:
Ajay Rahul Esha Omkar Ishita Neha
Sample Output
Second Highest Age : 55
Senior Employees : 4
Unique Ages : [34, 55, 29, 60, 42, 51]
Names Starting with Vowel : 3
Longest Employee Name : Ishita
Instructions
Implement all operations using separate functions.
Each function must accept parameters and return the result.
Do not print results inside the functions.
The menu should continue to appear until the user selects Exit.
Display an appropriate message for an invalid choice.
Use meaningful function and variable names and follow proper indentation
'''
def emp_names(n):
    emp_n = []
    for i in range(n):
        emp_n.append(input("Enter Name: "))
    return emp_n

def emp_ages(n):
    emp_a = []
    for i in range(n):
        emp_a.append(int(input("Enter Age: ")))
    return emp_a

def find_second_highest_age(emp_a):
    n_age = []

    for age in emp_a:
        if age not in n_age:
            n_age.append(age)

    n_age.sort()
    return n_age[-2]

def count_senior_employees(emp_a):
    count = 0 
    for age in emp_a:
        if age >= 50:
           count += 1
    return count    

def remove_duplicate_ages(emp_a):
    n_age = []

    for age in emp_a:
        if age not in n_age:
            n_age.append(age)

    
    return n_age 


def count_names_starting_with_vowel(emp_names):
    
    res = [] 
    for name in emp_names:
        if name.startswith(("A","E","I","O","U")):
            res.append(name)
            
    return len(res) 


def longest_name(emp_names):
    long = emp_names[0]
    for i in range(len(emp_names)):
         if  len(emp_names[0]) < len(emp_names[i]):
              
            emp_names[0] = emp_names[i]
    return emp_names[0]

def main():
    n = int(input("Enter N: "))

    names = emp_names(n)
    ages = emp_ages(n)

    print(names)
    print(ages)
    print("Second Highest Age:", find_second_highest_age(ages))
    print("Senior Employees :",count_senior_employees(ages))
    print("Unique Ages :", remove_duplicate_ages(ages))
    print("Names Starting with Vowel :",count_names_starting_with_vowel(names))

    print("Longest Employee Name :", longest_name(names))
main()



