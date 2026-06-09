'''
4.Find All Characters with Maximum Frequency
Website Traffic Analysis System

A web analytics company tracks user activity symbols in server logs.

The company wants to identify all characters having the maximum frequency in the given string.

Input:
aabbbccddd
Output:
b d
'''
s = input('Enter the string: ')
max_c = 0
res = ''
for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        temp = ''
        if s[j] == s[i]:
           temp = s[j]
           count += 1
    if count > max_c:
       max_c= count
       res = s[i]

    elif count == max_c:
        if s[i] not in res:
            res += ' ' + s[i]

print(res) 

             
  


