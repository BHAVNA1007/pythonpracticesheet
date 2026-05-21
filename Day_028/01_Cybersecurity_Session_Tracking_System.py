'''
1.Find the Longest Substring Without Repeating Characters
Cybersecurity Session Tracking System

A cybersecurity company monitors user session IDs generated during secure login sessions.

To detect suspicious repeated patterns, the company wants a Python program that finds the longest substring containing no repeated characters.
Input:
abcabcbb
Output:
abc
'''
s = input('Enter the string: ')
long =''

for i in range(len(s)):
   temp = ''
   for j in range(i,len(s)):
       if s[j] not in temp:
          temp += s[j]
       if len(temp)>len(long):
          long = temp   
       else:
          break
print(long)                       
          
            
 
