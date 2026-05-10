'''Assignment 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0'''

mobile_price, down_payment, interest_rate, months = map(int,input().split())
print(f"Mobile price = {mobile_price}")
print(f"Down payment = {down_payment}")
print(f"Interest rate = {interest_rate}%")
print(f"Months = {months}")

remaining_amount = mobile_price - down_payment
print(f"Remaining Amount = {remaining_amount}")
total_with_interest = remaining_amount+(remaining_amount * (10/100))
print(f"Total with Interest = {total_with_interest}")
monthly_emi = total_with_interest/months
print(f"Monthly EMI = {monthly_emi}")



