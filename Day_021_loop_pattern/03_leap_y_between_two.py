'''
03_leap_y_between_two
WAP to find out all the leap years between two entered years

'''

s = int(input("Enter starting year:"))
e = int(input("Enter ending year:"))

for year in range(s,e+1):

   if year%4==0 and (year%400==0 or year%100!=0):
       print(year) 
       count+=1
