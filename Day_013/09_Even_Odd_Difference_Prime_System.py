'''9.Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime
'''
import math
num = int(input("Enter a number = "))

even_count = 0
odd_count = 0

while num > 0:
      digit = num % 10
      if digit % 2 == 0:
          even_count  += 1
      else:
          odd_count += 1
      num = num // 10
diff = abs(even_count - odd_count)
print("Even Count =", even_count )
print("odd Count =", odd_count )
print("Difference =", diff )

if diff <= 1:
    print("Not prime")
else:
    x = 0
    i = 2
    while i <= math.sqrt(diff):
        if n % i == 0:
            x = 1
            break
        i += 1
    if x == 0:
         print("Prime")
    else:
         print("Not Prime") 
 