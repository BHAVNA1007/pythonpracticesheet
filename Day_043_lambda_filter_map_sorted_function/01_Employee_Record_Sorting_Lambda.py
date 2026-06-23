'''
1.Employee Record Sorting (Lambda)

A company stores employee details as (Name, Salary). The HR department wants to sort the employees based on salary.

Task

Write a Python program to sort the employee records using a lambda expression.

Input
employees = [("Rahul",45000),("Amit",30000),("Neha",55000),("Priya",40000)]
Output
[('Amit', 30000), ('Priya', 40000), ('Rahul', 45000), ('Neha', 55000)]
'''

record = []
n = int(input("N: "))

for i in range(n):
   name = input("Enter name: ")
   salary = int(input("Enter salary: "))
   info = (name, salary)
   record.append(info)
#print(record)

result = sorted(record, key=lambda s : s[1])
print(result)
 




