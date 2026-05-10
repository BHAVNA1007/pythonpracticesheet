'''3. Composite Number Detector

A product testing company labels batch numbers as risky if they have more than two factors. Such numbers are known as composite numbers and indicate repeated grouping patterns.

The quality control officer enters a batch number, and the software checks whether it is Composite or Not.

Write a program to check whether a number is Composite or Not.

Input:
12

Output:
Composite Number
'''

'''
using for loop

import math
n = int(input("Enter a number = "))

if n <= 1:
   print("Composite Number")

else:
    for i in range(2, int(math.sqrt(n))):
          if n % i == 0:
              print("Composite Number")
              break
    else:
         print("Not composite ")
'''
#using while loop

import math

n = int(input("enter the number = "))

if n <= 1:
   print("Composite number") 

else:
   x = 0
   i = 2
   while n <= int(math.sqrt(n)):
      if n % i == 0:
         x = 1
         break
      i += 1
   if x == 0:
       print("prime")
   else:
       print("Composite number") 
         
          
                  





          
    