'''Assignment 14: Simple Profit or Loss Calculator

Write a Python program that:

Accepts cost price and selling price.
Calculates profit/loss and percentage.

Input:
Cost Price = 1000
Selling Price = 1200

Output:
Profit = 200
Profit % = 20.0'''

cost_price,selling_price = map(int,input().split())
print(f"Cost Price = {cost_price}")
print(f"Selling Price = {selling_price}")
profit = selling_price - cost_price
print(f"Profit ={profit}")
profit_percentage = (profit/cost_price)*100
print(f"Profit % ={profit_percentage}")