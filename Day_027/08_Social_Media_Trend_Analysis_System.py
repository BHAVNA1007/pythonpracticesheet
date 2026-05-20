'''
Find the Second Highest Repeating Character in a String

Social Media Trend Analysis System

A social media company analyzes hashtags and user comments to identify trending character patterns.

The analytics team wants a Python program to find the character with the second highest frequency in a given string.

This helps detect secondary trending patterns in user activity.

Input:

aaabbbbccddeee

Output:

e

Explanation:

b occurs 4 times → highest
e occurs 3 times → second highest

Condition:

Program should work for both uppercase and lowercase letters.
Spaces should be ignored.
If no second highest frequency exists, print:
Second highest repeating character not found
'''

s = input('Enter The String: ')

s = s.replace(' ','')

i =0
unique = ''

while i <len(s):
   if s[i] not in unique:
       unique += s[i]
   i += 1

hg = 0
shg = 0
hg_ch=''
shg_ch=''    

i = 0

while i <len(unique):
    count = 0
    j = 0
    while j < len(s):
        if unique[i]==s[j]:
           count += 1
        j += 1

    if count > hg:
       shg = hg
       shg_ch = hg_ch
    
       hg = count
       hg_ch = unique[i] 

    elif count > shg and count != hg:
       shg = count
       shg_ch =unique[i]

    i += 1

if shg == 0:
    print("Second highest repeating character not found")  

else:
    print(shg_ch) 
     






