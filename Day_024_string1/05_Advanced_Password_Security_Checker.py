'''
5.Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password

'''
pwd = input("Enter a password: ")
upr = 0
digit = 0
space = 0
lwr = 0
special = 0
i = 0
while i < len(pwd):
    ch = pwd[i] 
    if ch.isupper():
        upr += 1

    elif ch.islower():
        lwr += 1

    elif ch.isdigit():
        digit += 1

    elif ch.isspace():
        space += 1

    else:
         special += 1
    i + 1

if len(pwd)>=8 and len(pwd)<=15 and  upr == 1 and  lwr == 1 and digit == 1 and space == 1 and  special == 1 and pwd[0]==pwd.upper() and len(n-1)==pwd.digit:

     print(" Secure Password")

else:

     print('not Secure Password')   

    
