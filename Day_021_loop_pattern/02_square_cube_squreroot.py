'''
02_square_cube_squreroot
WAP to print Square, Cube and Square Root of all numbers from 1 to N
'''

import math

n = int(input("Enter a number: "))
i = 1
while i <= n:  
   square = i**2
   print(f"\nSquare of {i} is = {square}")
   cube = i**3
   print(f"Cube of {i} is = {cube}") 
   square_root = math.sqrt(i) 
   print(f"Square Root of {i} is = {square_root}")
   i += 1
    
    
 


    






