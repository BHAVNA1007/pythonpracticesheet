'''2. Multi Stage Prime Lock System

A smart locker opens only if final derived number is prime.

Write a program to:

- Find sum of digits
- Find product of digits
- Find difference between product and sum
- Count digits in difference
- Add digit count to difference
- Check whether final result is Prime or Not

Input:
234

Output:
Sum = 9
Product = 24
Difference = 15
Digits = 2
Final Result = 17
Prime
'''
import math

num = int(input("Enter the number = "))
original_num = num
sum = 0
product = 1

while num > 0:
    digit = num % 10
    sum += digit
    product *= digit
    num = num // 10
print("Sum = ", sum)
print("Product = ", product)

diff = abs(product - sum)
print("Difference = ", diff)

original_diff = diff
count = 0
while diff > 0:
     digit = num % 10
     count += 1
     diff = diff // 10
print("Digits = ", count)

f_result = original_diff + count
print("Final Result = ", f_result )

if f_result <= 1:
    print("Not Prime")
else:
    for i in range(2, int(math.sqrt(f_result))):
         if f_result % i == 0:
              print("Not prime")
              break
    else:
         print("Prime")     

    
