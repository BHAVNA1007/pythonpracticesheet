'''1.=========================================
ONLINE SHOPPING CART
====================

A shopping website stores purchased products in a dictionary where:
Key = Product Name
Value = Quantity Purchased

Write a program to:

* Accept a dictionary from the user.
* Calculate and display the total quantity of products purchased.

Sample Input:
{"Laptop":2,"Mouse":3,"Keyboard":1}

Sample Output:
Total Quantity = 6
'''
n = int(input("Enter size of dict: "))

d = {}

for i in range(n):
    key = input("Enter Key: ")
    value = int(input("Enter value"))
    d[key] = value
print(d)    

total = 0
for  v in d.values():
    total =total + v
    
print(total)    

'''
using build in function sum
t = sum(d.values())
print(t)
'''