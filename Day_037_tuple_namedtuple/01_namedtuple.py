'''
=====================================================
QUESTION 1: EMPLOYEE SALARY ANALYSIS
====================================

A company wants to store employee details and generate salary reports using NamedTuple.

Fields:
emp_id, emp_name, department, salary

Requirements:

1. Read N employee details from the user and store them in a list of NamedTuples.

---

2. Display all employee details.

---

3. Find and display the employee with the highest salary.

---

4. Find and display the employee with the lowest salary.

---

5. Calculate and display the average salary of all employees.

---

6. Accept a department name from the user and display all employees belonging to that department.

---

Test Case:

Input:
Enter number of employees: 4

101 Rahul IT 50000
102 Priya HR 45000
103 Amit IT 70000
104 Neha Finance 60000

Enter department: IT

Expected Output:
Highest Salary Employee:
103 Amit IT 70000

Lowest Salary Employee:
102 Priya HR 45000

Average Salary:
56250.0

Employees in IT Department:
101 Rahul IT 50000
103 Amit IT 70000
'''
from collections import namedtuple

n = int(input("Enter no of Employees:  "))

Employee = namedtuple("Employee",['emp_id', 'emp_name', 'department', 'salary'])

Namedtuples = []

for i in range(n):
   print(f"Enter Employee{i+1} details:")
   id = int(input("Enter employee id: "))
   name = input("Enter employee name: ")
   dep = input("Enter department: ")
   salary = float(input("Enter salary: "))
   Namedtuples.append(Employee(id,name,dep,salary))



for employee in Namedtuples:
    print(employee.emp_id,end=' ')
    print(employee.emp_name,end=' ')
    print(employee.department,end=' ')
    print(employee.salary,end=' ')
    print()

       
highest_s = Namedtuples[0]
for employee in Namedtuples:

    if  highest_s.salary < employee.salary:
        highest_s = employee
         

print("\nEmployee with Highest Salary: ")
print(highest_s.emp_id,end=' ')
print(highest_s.emp_name,end=' ')
print(highest_s.department,end=' ')
print(highest_s.salary,end=' ')
print()

lowest_s = Namedtuples[0]
for e in Namedtuples:

    if  lowest_s.salary > e.salary:
        lowest_s = e
         

print("\nEmployee with lowest Salary: ")
print(lowest_s.emp_id,end=' ')
print(lowest_s.emp_name,end=' ')
print(lowest_s.department,end=' ')
print(lowest_s.salary,end=' ')
print()

count = 0
sum = 0
for employee in Namedtuples:
   count += 1
   sum += employee.salary
   avg = sum / count

print("\nAverage Salary", avg)



print("\nEmployees in IT department: ")   
dep = input("\nEnter department: ")   
for employee in Namedtuples:
   
   if employee.department == "IT":
       print(employee.emp_id,end=' ')
       print(employee.emp_name,end=' ')
       print(employee.department,end=' ')
       print(employee.salary,end=' ')
       print()

