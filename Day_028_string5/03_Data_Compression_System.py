'''
3.Replace Consecutive Duplicate Characters with Single Character
Data Compression System

A cloud storage company wants to reduce unnecessary repeated characters in text logs.

Write a Python program that replaces consecutive duplicate characters with a single occurrence.

Input:
aaabbbccccdddaa
Output:
abcda
'''
s = input('Enter the string: ')
curr = ''
prev = ''
res =s[0] 
for i in range(1,len(s)):
    curr=s[i]
    prev = s[i-1]
    if curr != prev:
       
       res += curr 
print(res)
    