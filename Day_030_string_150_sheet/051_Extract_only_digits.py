'''
051_Extract_only_digits
S = "a1b2c3" "123"
'''
s = input('Enter the string: ')
n_s = ''

for i in range(len(s)):
   ch = s[i]
   if ch >= '1' and ch <= '9':
      n_s += ch
 
print(n_s)