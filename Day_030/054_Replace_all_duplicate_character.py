'''
054_Replace_all_duplicate_characters with '$'.
 S = "hello" "he$lo
'''

s = input('Enter the string: ')

temp =''

for i in range(len(s)):
    if s[i] in temp:
       temp += "$"
    else:
       temp += s[i]

print(temp) 