'''
053_Remove_all_punctuation_characters
S = "Hello, world!" "Hello world"
'''

s = input('Enter the string: ')
n_s =''

for i in range(len(s)):
   ch = s[i]
   if ch>='a' and ch<='z' or ch>='A' and ch<='Z' or ch == " ":
      n_s += ch 
   
print(n_s)


