'''
057_Merge_two_strings_alternatively 
(char by char). S1 = "ABC", S2 = "def" "AdBeCf"

'''

s1 = input('Enter a string: ')
s2 = input('Enter a string: ')

res = ''

for i in range(len(s1)):
    res += s1[i]
    res += s2[i]
print(res)  