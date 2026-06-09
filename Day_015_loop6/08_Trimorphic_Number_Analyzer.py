'''8.Trimorphic Number Analyzer

A coding system checks cube-based patterns.

A Trimorphic Number:
Cube of number ends with the same number.

Example:
4³ = 64

Write a program to check Trimorphic Number.

Input:
4

Output:
Trimorphic Number
'''

num = int(input("Enter The number = "))

cube = num**3

while num > 0:

   if num % 10 == cube % 10 :
    
       print("Trimorphic Number")
       break

   else:
       print("Not Trimorphic Number")
       break

                     
   
       
