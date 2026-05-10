'''Assignment 6: Discount Calculator

Write a Python program that:

Accepts total amount.
Calculates 10% discount and final price.

Input:
Amount = 1000

Output:
Discount = 100
Final = 900
-----------------------------------'''

amount = int(input())
print(f"Amount = {amount}")
discount = amount*(10/100)
print(f"Discount = {discount}")
final = amount - discount
print(f"Final = {final}")

