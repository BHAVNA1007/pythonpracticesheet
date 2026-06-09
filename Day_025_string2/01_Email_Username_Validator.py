'''
1.
Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username
'''
u_name = input('Enter a UserName: ')
l = len(u_name)

if l >= 5 and l<=12:
    if (u_name[0]>='a' and u_name[0]<='z') or (u_name[0]>='A' and u_name[0]<='Z'):

       valid = True
       
       for ch in u_name:
           if(ch >= 'a' and ch <= 'z') or \
             (ch >= 'A' and ch <= 'Z') or \
             (ch >= '0' and ch <= '9') or ch=='_':
               pass
           else:
               valid = False
               break 
       
       if valid:
               print("Valid username")
       else:
           print('Invalid username')
    else:
         print('Invalid username')
else:
    print('Invalid username')         

      
                      








