'''
5. Find the Number of Unique Characters in a String

Password Strength Analyzer

A cybersecurity company checks password strength based on the number of unique characters present.

Passwords containing more unique characters are considered more secure.

Write a Python program to count the number of unique characters in a string.

Input:
aabbccdde

Output:
5
'''
s = input('Enter the string: ')

i = 0
uniq =''
while i<= len(s)-1:
   ch = s[i]
   count = 0
   j = 0
   while j <= len(uniq)-1:
       if ch == uniq[j]:
           count += 1
       j += 1  
   if count == 0:
      uniq += ch       
  
   i += 1

print(len(uniq))
   
   
   
