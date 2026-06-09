'''9.Abundant Number Detector

A financial system analyzes surplus numbers.

An Abundant Number:
Sum of proper factors > number

Write a program to check Abundant Number.

Input:
12

Output:
Abundant Number
'''
import math
num = int(input("Enter The number = "))

sum_of_factors = 0
for i in range(1, num // 2 + 1):
    if num % i == 0:
       sum_of_factors = sum_of_factors + i
       
      


if sum_of_factors > num :

     print("Abundant Number")

else:
     print("Not Abundant Number") 



    
