'''
103 Check if a string contains balanced parentheses. 
S = "((()))" TRUE

'''

s = input("Enter paranthisis: ")

open_paran = 0
close_paran = 0

for i in s:
   if i == "(":
       open_paran += 1
   elif i == ")":
       close_paran += 1  

if open_paran == close_paran:
   print("TRUE")

else:
   print("FALSE")