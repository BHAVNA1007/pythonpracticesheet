'''11.
=========================================
PRODUCT SALES ANALYSIS
======================

sales = [
"Mobile",
"Laptop",
"Mobile",
"Tablet",
"Laptop",
"Mobile"
]

Write a program to:

* Count sales of each product.
* Display products in sorted order.

Sample Output:
Laptop : 2
Mobile : 3
Tablet : 1
'''
n = int(input("Enter num of sales: "))

sales = []
for s in range(n):
    sales.append(input())
print(sales)

s = {}
for i in sorted(sales):
    s[i] =s.get(i,0)+1
print(s)    