
'''========================================
Assignment 8: Simple Interest Calculator
========================================

A bank wants to help customers calculate the simple interest on their savings.

Write a Python program that:
- Accepts principal amount, rate of interest, and time (in years) as input.
- Calculates the simple interest using the formula:
  SI = (P × R × T) / 100
- Displays the simple interest.

Example:
Principal = 1000
Rate = 5
Time = 2
Simple Interest = 100.0
-----------------------------------------------'''


principal = int(input("Principal = "))
rate = int(input("Rate = "))
time,year = input("Time = ").split()
SI = (principal * rate * int(time) ) / 100
print("Simple Interest =",SI)



