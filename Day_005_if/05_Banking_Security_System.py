'''
05_Banking_Security_System
   A bank validates login attempt:

* If username is "admin" → Valid user
* If password length ≥ 8 → Strong password

Input:
Enter username: admin
Enter password: secure123

Output:
Valid user
Strong password '''

user_name = input("Enter username: ")
password = input("Enter password: ")

if user_name== "admin":
    print("Valid user")
if len(password)>= 8:
    print("Strong password")
   