'''
07_Enterprise_Password_Pattern_Strength_Analyzer

A cybersecurity company wants to validate advanced passwords.
## Conditions:
* Minimum 10 characters
* At least:

  * 1 uppercase letter
  * 1 lowercase letter
  * 1 digit
  * 1 special character
* No consecutive repeating characters
* No spaces allowed

### Input:
text
Pyth@n1234

### Output:
text
Strong Password

### Input:
text
Paaass@12

### Output:
text
Weak Password
'''

s  = input('Enter the password: ')
up = 0
low = 0
di = 0
sc = 0
sp = 0
for i in range(len(s)):
    ch = s[i]
    if ch>='a' and ch<='z':
        low = 1
    elif ch>='A' and ch<='Z':   
        up = 1     
    elif ch >= '0' and ch<='9'
        di = 1
    else:
        sc = 1 

if (ch >='a'  or ch<='z') and


