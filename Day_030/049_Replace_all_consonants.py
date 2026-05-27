'''
49 Replace all consonants with '*' (Example suggests replacing non-vowels). S = "apple" "ap*le" (or similar output depending on implementation)
'''

s = input("Enter the string: ")
new_s = ''
for i in range(len(s)):
    ch = s[i]
    if ch!='a' and ch!='e' and ch!='i' and ch!='o' and ch!='u':
         
        new_s += "*"
    else:
        new_s += ch 

print(new_s)