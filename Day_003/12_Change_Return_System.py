'''Assignment 12: Change Return System

Write a Python program that:

Accepts amount.
Calculates ₹100, ₹50, ₹10 notes.

Input:
Amount = 380

Output:
₹100 x 3
₹50 x 1
₹10 x 3'''

amount = int(input())
print(f"Amount = {amount}")
rem1 = amount % 100
qut1 = amount // 100
rem2 = rem1 % 50
qut2 = rem1 // 50
rem3 = rem2 % 30
qut3 = rem2 // 30
print(f"₹100 x {qut1}")
print(f"₹50 x {qut2}")
print(f"₹30 x {qut3}")

