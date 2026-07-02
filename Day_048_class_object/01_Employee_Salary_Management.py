'''
Question 1: Employee Salary Management System
Scenario

A company wants to automate employee salary calculations. The HR department needs a system that calculates the gross salary of an employee by including allowances.

Requirements

Create a class named Employee with the following attributes:

employee_id
employee_name
basic_salary

Initialize the values using a constructor.

Calculations
HRA = 20% of Basic Salary
DA = 15% of Basic Salary
Gross Salary = Basic Salary + HRA + DA
Sample Input
Enter Employee ID : E101
Enter Employee Name : Rahul Sharma
Enter Basic Salary : 50000
Sample Output
------ Employee Salary Details ------
Employee ID      : E101
Employee Name    : Rahul Sharma
Basic Salary     : 50000.0
HRA              : 10000.0
DA               : 7500.0
Gross Salary     : 67500.0
'''


class Employee:

     def __init__(self, employee_id, employee_name, basic_salary):

         self.id = employee_id 
         self.name = employee_name 
         self.salary = basic_salary 

     
         self.HRA = self.salary * 0.2 
         self.DA = (self.salary * 15)/100
         self.Gross_Salary =  self.salary + self.HRA + self.DA
          
def main():
    employee_id = input("Enter Employee ID: ")
    employee_name = input("Enter Employee Name : ")
    basic_salary = int(input("Enter Basic Salary : "))

    e1 = Employee(employee_id, employee_name, basic_salary)
    
     
 
    print("\n------ Employee Salary Details ------\n")
    print("\nEmployee ID    :", e1.id) 
    print("Employee Name    :", e1.name) 
    print("Basic Salary     :", e1.salary) 
    print("HRA              :", e1.HRA)
    print("DA               :", e1.DA)
    print("Gross Salary     :", e1.Gross_Salary)
    

main()
  
    
    


 