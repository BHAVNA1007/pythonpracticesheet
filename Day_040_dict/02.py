'''
2.
=========================================
EMPLOYEE DEPARTMENT COUNT
=========================

A company stores employee department names in a list.

employees = ["HR","IT","HR","Sales","IT","IT","Finance"]

Write a program to:

* Count how many employees belong to each department.
* Store the result in a dictionary.

Sample Output:
{'HR': 2, 'IT': 3, 'Sales': 1, 'Finance': 1}
---
'''
n = int(input("Enter size of com: "))

em = []
for i in range(n):
    em.append(input())
print(em)  

d = {}
  
for e in em:
  d[e] = d.get(e,0)+1
print(d)  
  
  
  
        
        

