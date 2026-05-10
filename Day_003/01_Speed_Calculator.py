'''Assignment 1: Speed Calculator

Write a Python program that:

Accepts distance (in km) and time (in hours).
Calculates speed.

Input:
Distance = 120
Time = 2

Output:
Speed = 60 km/h
----------------------------------------'''

dis,time=map(int,(input()).split())
print(f"Distance = {dis}km")
print(f"Time = {time}hour")
speed = dis//time
print(f"Speed {speed} km/hour")