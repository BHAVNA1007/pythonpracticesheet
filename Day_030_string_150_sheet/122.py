'''
122 Convert a binary string to decimal. S = "101" 5

'''

s = input("S: ")

decimal = 0

for ch in s:

   decimal = decimal * 2 + int(ch)

print(decimal)