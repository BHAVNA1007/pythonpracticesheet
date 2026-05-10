'''Assignment 15: Average Speed for Multiple Trips

Write a Python program that:

Accepts distance1, time1, distance2, time2.
Calculates average speed.

Input:
Distance1 = 60
Time1 = 1
Distance2 = 40
Time2 = 1

Output:
Average Speed = 50 km/h'''

distance1,time1,distance2,time2 = map(int,input().split())
print(f"Distance1 ={distance1}")
print(f"Time1 ={time1}")
print(f"Distance2 ={distance2}")
print(f"Time2 ={time2}")
speed1 = distance1*time1
speed2 = distance2*time2
avg_speed = (speed1+speed2)//2
print(f"Average Speed = {avg_speed} km/h")