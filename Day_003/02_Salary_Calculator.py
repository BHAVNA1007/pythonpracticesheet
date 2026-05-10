'''Assignment 2: Salary Calculator

Write a Python program that:

Accepts daily wage and number of days.
Calculates total salary.

Input:
Daily wage = 500
Days = 26

Output:
Salary = 13000
----------------------------------------------'''

daily_wage,days = map(int,(input()).split())
print(f"Daily wage = {daily_wage}")
print(f"Days = {days}")
salary = daily_wage*days
print(f"Salary = {salary}")