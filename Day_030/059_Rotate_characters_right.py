'''
059_Rotate_characters_right by 3 positions
 S = "abcde" "cdeab"

'''

s = input('Enter the string: ')

s1 = s[-3:]
s2 = s[:-3]

print(s1+s2) 