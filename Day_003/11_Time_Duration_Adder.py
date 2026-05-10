'''Assignment 11: Time Duration Adder

Write a Python program that:

Accepts hours, minutes, seconds.
Converts into total seconds.

Input:
Hours = 1
Minutes = 2
Seconds = 30

Output:
Total Seconds = 3750'''

hours,minutes,seconds = map(int,input().split())
print(f"Hours = {hours}")
print(f"Minutes = {minutes}")
print(f"Seconds = {seconds}")
total_seconds = (hours*3600)+(minutes*60)+(seconds)

print(f"Total Seconds ={total_seconds}")
