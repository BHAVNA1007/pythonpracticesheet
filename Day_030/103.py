'''
103 Check if a string contains balanced parentheses. 
S = "((()))" TRUE

'''

s=input("Enter s: ")
open_p=0
close_p=0
for i in s:
    if i=="(":
        open_p+=1
    elif  i==")":
        close_p+=1
if open_p==close_p:
    print("True")
else:
    print("False")