'''
Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4 '''



second =int( input("Total seconds = "))

hour = second // 3600
reminder = second % 3600
minute = reminder//60
reminder = reminder%60
print(f"Hours = {hour}") 
print(f"Minutes = {minute}")
print(f"Seconds = {reminder}")

