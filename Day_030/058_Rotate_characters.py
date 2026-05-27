'''
058_Rotate_characters left by 2 positions
 S = "abcde" "cdeab
'''

s = input('Enter the string: ')

s1 = s[2:]
s2 = s[0:2]

res = s1 + s2

print(res)