'''Assignment 5: Average Marks Calculator

Write a Python program that:

Accepts marks of 3 subjects.
Calculates average.

Input:
Marks = 80, 90, 70

Output:
Average = 80.0
-----------------------------------------------'''

math,eng,hindi= map(int,input().split())
print(f"Marks = {math}, {eng}, {hindi}")
avg = (math+eng+hindi)/3
print(f"Average = {avg}")
