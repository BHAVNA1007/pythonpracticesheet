'''
048_Remove_all_vowels 
S = "aeiou XYZ" " XYZ"
'''
s = input('Enter the string: ')

new_s = ''

for i in range(len(s)):
   ch = s[i]
   if ch!='a' and ch!='e' and ch!='i' and ch!='o' and ch!='u':
        new_s += s[i]    
print(new_s)
     