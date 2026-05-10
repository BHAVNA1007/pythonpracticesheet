'''
Assignment 9: Petrol Cost Calculation

You traveled a certain distance. Based on mileage and petrol price, calculate fuel used and total cost.

Input:
Distance = 450 km
Mileage = 15 km/litre
Petrol price = 110/litre

Expected Output:
Petrol Used = 30.0 litres
Total Cost = 3300.0 '''

dis, mile, p_price = map(int,input().split())
print(f"Distance = {dis} km")
print(f"Mileage = {mile} km/liter")
print(f"Petrol price = {p_price}/liter")
p_used = dis/mile
print(f"trol Used = {p_used} liters")
t_cost = p_used * p_price
print(f"Total Cost = {t_cost}")