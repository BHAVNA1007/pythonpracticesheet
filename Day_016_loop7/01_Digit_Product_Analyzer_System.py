'''1.Digit Product Analyzer System

A data analytics company studies patterns in numeric transaction IDs to detect hidden behaviors.

For every entered number, the system analyzes relationships between its digits.

Write a program to:

Find the product of every pair of adjacent digits
Display all the products
Find the sum of all these products
Find the smallest product value
If the sum of products is divisible by the total number of digits, print Stable Number
Otherwise print Unstable Number

Use loops wherever required.

Input:
57294

Output:
Products: 35 14 18 36
Sum = 103
Smallest = 14
Unstable Number
'''
'''
num = int(input("Enter The Number = "))

origenal = num
l = len(str(num))
sum = 0
smallest = 999

while num > 9:
  
   d1 = num % 10
   d2 = (num // 10)  % 10
   product = d1 * d2
   print(product,end=" ")
   
   sum +=product    
   num = num // 10
  
   if product < smallest:
       smallest = product
   
print("\nSum =",sum)
print("Smallest ="smallest)

count = 0


while origenal > 0:
    d = origenal % 10
    count += 1
    origenal = origenal // 10
print(count)

if sum % count == 0:
   print("Stable number")
else:
   print("Unstable Number")


'''

num = input("Enter The number = ")

l = len(num)
sum = 0
smallest = 999
for i in range(l-1):
    d1 = int(num[i])
    d2 = int(num[i + 1]) 
    product = d1 * d2
    print(product,end = " ")
    sum += product
    if smallest > product:
       smallest = product

print("\nSum =",sum)

print("Smallest = ",smallest)

if sum % l == 0:
   print("Stable Number")
else:
   print("Unstable number")
   





 





