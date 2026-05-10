'''
4. E-Commerce Discount Engine


An online shopping platform provides discounts to customers based on their total purchase amount:

* Above ₹5000 → 20% discount
* ₹2000 to ₹5000 → 10% discount
* Below ₹2000 → 5% discount

Write a Python program to calculate the final amount after discount.

Input:
Enter purchase amount: 4500

Output:
Final Amount: ₹4050


'''
amount = int(input("Enter purchase amount: "))

if amount > 5000:
     dis = amount*20/100
     t_amount = amount - dis
     print(f"Final Amount: {t_amount}") 
else:
    if amount <= 5000:
        dis = amount*10/100
        t_amount = amount - dis
        print(f"Final Amount: {t_amount}") 
    else:
        dis = amount*5/100
        t_amount = amount - dis
        print(f"Final Amount: {t_amount}")
        


