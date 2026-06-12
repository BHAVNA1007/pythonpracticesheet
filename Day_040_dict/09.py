'''9.
=========================================
INVENTORY MANAGEMENT SYSTEM
===========================

Store product stock in a dictionary.

stock = {
"Pen":50,
"Pencil":100,
"Eraser":25,
"Marker":10
}

Write a program to:

* Display products having stock less than 30.

Sample Output:
Eraser
Marker
'''
n = int(input("Enter num of products: "))

stock = {}
for s in range(n):
    key = input("Product: ")
    value = int(input("stock: "))
    stock [key] = value
print(stock )    

for p, s in stock .items():
    if s  <  30:
        print(p) 