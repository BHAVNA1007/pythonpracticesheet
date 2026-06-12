'''
6.
=========================================
MOBILE APP DOWNLOAD COUNTER
===========================

Downloads received from different cities:

cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]

Write a program to:

* Count downloads city-wise.
* Display city with maximum downloads.

Sample Output:
{'Indore':3,'Bhopal':1,'Pune':2,'Delhi':1}
Most Downloads : Indore
'''
n = int(input("Enter num of city: "))

cities = []
for p in range(n):
    cities.append(input())
print(cities)

c = {}
for city in cities:
    c[city] = c.get(city, 0)+1
print(c)


h_d= -1
h_name = ""
for k, v in c.items():
    if v  >  h_d:
            h_d = v
            h_name = k
print("Most Downloads :", h_name)             