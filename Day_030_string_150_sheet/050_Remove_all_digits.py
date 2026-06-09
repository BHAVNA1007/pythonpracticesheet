'''
050_Remove_all_digits
S = "a1b2c3" "abc"
'''
s = input('Enter the string: ')
new_s = ''

for i in range(len(s)):
   ch = s[i]
   if ch>='a' and ch<='z':
      new_s += ch

print(new_s)   