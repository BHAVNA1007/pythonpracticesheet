'''
4.Electricity Billing System
An electricity board calculates bills based on units consumed:
Up to 100 units → ₹5 per unit
101–300 units → ₹7 per unit
Above 300 units → ₹10 per unit
Write a program to compute total bill using inline if.
'''

u = int(input("Enter units = "))

bill = u * 5 if u <= 100 else ((100*5) +((u-200)*7)) if u>100 and u <= 300 else ((100*5)+(200*7))+((u-300)*10)

print("Bill = ", bill)