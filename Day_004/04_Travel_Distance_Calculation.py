'''Assignment 4: Travel Distance Calculation

A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

Input:
Speed = 60 km/hr
Time = 2 hours 30 minutes

Expected Output:
Total Time = 2.5 hours
Distance = 150.0 km
'''

speed,t_hour,t_min = map(int,input().split())
print(f"Speed = {speed} km/hr")
print(f"Time = {t_hour} hours {t_min} minutes")

total_time = t_hour + (t_min)/60
print(f"Total Time = {total_time } hours")
distance = speed * total_time
print(f"Distance = {distance}km")


  


