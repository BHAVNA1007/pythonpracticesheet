'''
1. Smart Shopping Mall Discount System
A shopping mall offers discounts based on customer type and purchase amount.
If the customer is premium, they get 20% discount when the amount is more than 5000, otherwise 10%.
If the customer is regular, they get 10% discount when the amount is more than 3000, otherwise 5%.
Write a program to calculate the final payable amount using inline if only.
'''

amt = int(input("Enter The Amount = "))

ctm = input("Enter the Type = ")

discount = amt * 20/100 if amt > 5000 and ctm =='premium' else amt * 10/100 if amt > 3000 and ctm =='regular' else amt*5/100
print("Discount = ",discount)

