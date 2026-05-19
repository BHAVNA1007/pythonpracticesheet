'''
1_Bank_Customer_Account_Privacy_System

A national bank is developing a secure customer portal where account
numbers should not be displayed completely on the screen. For security
reasons, the system should hide all digits except the last four digits
before showing them to users.

Conditions: - Display only the last 4 digits - Replace all previous
characters with *

Input: Enter account number: 123456789012

Output: Masked Account: ****9012
'''
a_num = input('Enter account number: ')
l =len(a_num)

star = ''
num = ''

for i in range(l-4):
    star = star + "*"


for i in range(l-4,l):
    num += a_num[i]
secure_ac = star +num
print(secure_ac)




    

