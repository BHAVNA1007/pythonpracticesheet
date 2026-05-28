'''
61 Count total alphabets, digits, and special characters. S = "a1b!c2" Alphabets: 3, Digits: 2, Special: 1
'''

s = input('Enter a string: ')

alpha = 0
digit = 0
s_char = 0

for i in range(len(s)):
  ch = s[i]
  if ch>='a' and ch<='z':
      alpha += 1
  elif ch>='0' and ch<='9': 
      digit += 1
  else:
      s_char += 1
print("Alphabets: ", alpha)
print("Digits: ", digit)
print("Special: ", s_char)  
  


