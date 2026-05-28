'''
62 Count vowels and consonants. S = "apple" Vowels: 2, Consonants: 3
'''

s = input('Enter the string: ')

vo = 0
cons = 0
for ch in s:
   if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
       vo += 1
   else:
       cons += 1

print("Vowels: ",vo)
print("Consonants:  ",cons)