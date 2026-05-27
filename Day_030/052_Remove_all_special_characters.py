'''
052_Remove_all_special_characters
S = "a!@b#c" "abc
'''

s = input('Enter the string: ')
n_s =''

for i in range(len(s)):
   ch = s[i]

   if ch>='a' and ch<='z':
      n_s += ch
print(n_s)    
