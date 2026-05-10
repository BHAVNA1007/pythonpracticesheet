'''
6. Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2
'''

import math
num = int(input("Enter The Number = "))

if num <= 1 :
    

    print("Composite")

else:
    x = 0
    i = 2
    while i <= num+1 :
          if num % i == 0:
              x = 1 
              small = i
              break
          i += 1
    if x == 1:
        
         print("Composite") 
         factor = 1
         count = 0
         while factor<= num:
            if num % factor == 0:
                count += 1
            factor += 1
         print("Factors count = ",count)
    print("Smallest Factore = ", small)   
           









        
    
         

