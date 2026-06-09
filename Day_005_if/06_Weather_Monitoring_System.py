'''
06_Weather_Monitoring_System
   A system checks weather conditions:

* If temperature ≥ 30 → Hot day
* If humidity ≥ 70 → High humidity alert

Input:
Enter temperature: 32
Enter humidity: 75

Output:
Hot day
High humidity alert'''

temperature = int(input("Enter temperature: "))
humidity = int(input("Enter humidity: "))

if temperature>=30:
    print("Hot day")
if humidity>=75:
    print("High humidity alert")