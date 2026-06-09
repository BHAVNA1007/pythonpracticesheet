'''
68 Count the sum of digits present in a string. 
S = "a1b2c3" 6 (1+2+3)
'''

s = input('Enter a string: ')

sum = 0

for i in range(len(s)):
   ch = s[i]
   if ch >='0' and ch <= '9':
        sum += int(ch) 
print(sum) 

