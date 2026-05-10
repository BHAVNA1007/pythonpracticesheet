'''Assignment 9: Fuel Cost Calculator

Write a Python program that:

Accepts distance (km), mileage (km/litre), and petrol price.
Calculates total fuel cost.

Input:
Distance = 100
Mileage = 20
Petrol Price = 100

Output:
Cost = 500'''

distance,mileage,petrol_price = map(int,input().split(maxsplit=2))
print(f"Distance = {distance}")
print(f"Mileage = {mileage}")
print(f"Petrol Price = {petrol_price}")
cost = (distance*petrol_price)//mileage
print(f"Cost = {cost}")