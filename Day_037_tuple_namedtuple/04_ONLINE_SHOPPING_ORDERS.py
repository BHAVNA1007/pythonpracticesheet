'''
QUESTION 4: ONLINE SHOPPING ORDERS
==================================

An online shopping company stores customer orders using NamedTuple.

Fields:
order_id, customer_name, product_name, amount

Requirements:

1. Read N order records from the user and store them in a list of NamedTuples.

---

2. Display all order details.

---

3. Find and display the order having the highest amount.

---

4. Calculate and display total sales.

---

5. Count the number of orders whose amount is greater than ₹10,000.

---

Test Case:

Input:
Enter number of orders: 5

O101 Rahul Laptop 55000
O102 Priya Mouse 800
O103 Amit Mobile 25000
O104 Neha Keyboard 1500
O105 Rakesh TV 45000

Expected Output:
Highest Value Order:
O101 Rahul Laptop 55000

Total Sales:
127300

Orders Above ₹10,000:
3
'''


from collections import namedtuple

n = int(input("Enter no of orders:  "))

order = namedtuple("order",['order_id','customer_name', 'product_name','amount'])

orders = []

for i in range(n):
   print(f"Enter order{i+1} details:")
   o_id = input("Enter order id: ")
   c_name = input("Enter customer name: ")
   p_name = input("Enter  product name: ")
   amt = int(input("Enter amount: "))
   orders.append(order(o_id,c_name,p_name,amt))



for o in orders:
    print(o.order_id,end=' ')
    print(o.customer_name,end=' ')
    print(o.product_name,end=' ')
    print(o.amount,end=' ')
    print()

       
Highest_v_o = orders[0]
for o in orders:

    if  Highest_v_o.amount < o.amount:
        Highest_v_o = o
         

print("\nHighest Value Order: ")
print(Highest_v_o.order_id,end=' ')
print(Highest_v_o.customer_name,end=' ')
print(Highest_v_o.product_name,end=' ')
print(Highest_v_o.amount,end=' ')
print()


count = 0
for o in orders:

    if  o.amount > 10000:
        count += 1
         
print("Orders Above ₹10,000: ")
print(count)
print()

total_sale = 0
for o in orders:
   
   total_sale += o.amount

print("\nTotal Sales:", total_sale)


