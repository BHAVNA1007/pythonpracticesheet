'''12.
=========================================
ONLINE FOOD DELIVERY ANALYSIS
=============================

orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]

Write a program to:

* Count orders of each food item.
* Find the most ordered item.

Sample Output:
Pizza : 3
Burger : 2
Pasta : 2

Most Ordered : Pizza
'''
n = int(input("Enter num of orders: "))

orders = []
for o in range(n):
    orders.append(input())
print(orders)

s = {}
for i in orders:
    s[i] =s.get(i,0)+1
print(s)    

m_o= -1
m_name = ""
for k, v in s.items():
    if v  >  m_o:
            m_o = v
            m_name = k
print("Most Ordered :", m_name)             