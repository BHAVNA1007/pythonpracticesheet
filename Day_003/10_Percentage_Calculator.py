'''Assignment 10: Percentage Calculator

Write a Python program that:

Accepts total marks and obtained marks.
Calculates percentage.

Input:
Total = 500
Obtained = 400

Output:
Percentage = 80%'''

total_marks,obtained_marks = map(int,input().split())
print(f"Total = {total_marks}")
print(f"Obtained = {obtained_marks}")
percentage = (obtained_marks/total_marks)*100
print(f"Percentage = {percentage}%")