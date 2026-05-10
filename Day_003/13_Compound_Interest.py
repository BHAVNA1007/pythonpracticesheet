'''Assignment 13: Compound Interest Calculator

Write a Python program that:

Accepts principal, rate, and time.
Calculates compound interest.

Input:
Principal = 1000
Rate = 10
Time = 2

Output:
Amount = 1210.0
Compound Interest = 210.0'''



principal,rate,time = map(int,input().split(maxsplit=3))
print(f"Principal ={principal}")
print(f"Rate ={rate}")
print(f"Time ={time}")
amount = round(principal*((1+rate/100)**time),1)
#a = principal * pow((1 + rate/100),time)
print(f"Amount = {amount}")
compound_interest = round(amount - principal,1)
print(f"Compound Interest = {compound_interest}")


