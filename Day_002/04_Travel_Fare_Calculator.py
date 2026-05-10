'''========================================
Assignment 4: Travel Fare Calculator
========================================

A cab company charges ₹15 per kilometer.

Write a Python program that:
- Accepts the number of kilometers traveled.
- Calculates the total fare.
- Displays the result.

Example:
Distance = 20 km
Total fare = ₹300

-------------------------------------------------'''

distance,unit = input("Distance = ").split()
total_fare = int(distance)*15
print(f"Total fare = ₹{total_fare}")
