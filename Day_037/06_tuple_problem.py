'''
6.NOTE: using tuple only
An electronics store wants to maintain product information. Since product details should not be modified accidentally,
 each product record is stored as a tuple.

Tuple Format:

(product_id, product_name, price)

Requirements:

Read N product details from the user and store them as tuples in a list.
Display all product details.
Find and display the costliest product.
Find and display the cheapest product.
Calculate and display the average price of all products.
Display all products whose price is greater than ₹50,000.

Test Case:

Input:

Enter number of products: 4

P101 Laptop 65000
P102 Mobile 25000
P103 Television 80000
P104 Tablet 30000

Expected Output:

All Products:
('P101', 'Laptop', 65000)
('P102', 'Mobile', 25000)
('P103', 'Television', 80000)
('P104', 'Tablet', 30000)

Costliest Product:
('P103', 'Television', 80000)

Cheapest Product:
('P102', 'Mobile', 25000)

Average Price:
50000.0

Products Above ₹50,000:
('P101', 'Laptop', 65000)
('P103', 'Television', 80000)
'''
n = int(input("Enter no of products:  "))

products = []

for i in range(n):
   print(f"Enter product{i+1} details:")
   p_id = input("Enter product id: ")
   p_name = input("Enter  product name: ")
   price = int(input("Enter price: "))
   product = (p_id, p_name, price )
   products.append(product)



for p in products:
    print(p)

costly = products[0]
for p in products:
    if costly[2] < p[2]:
         costly = p
print("\nCostliest Product:")
print(costly)


Cheapest = products[0]
for p in products:
    if Cheapest[2] > p[2]:
         Cheapest = p
print("\nCheapest Product::")
print(Cheapest)


count = 0
sum = 0
for p in products:
   count += 1
   sum += p[2]
   avg = sum / count

print("\nAverage Price:", avg)


print("\nProducts Above ₹50,000: ")
for p in products:

    if  p[2] > 50000:
        print(p)   

