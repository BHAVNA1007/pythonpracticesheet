'''
1. Find the length of a string.
2. Copy one string to another.
3. Concatenate two strings.
4. Compare two strings (case-sensitive).
5. Compare two strings ignoring case.
6. Convert a string to uppercase.
7. Convert a string to lowercase.
8. Toggle the case of each character in a string.
9. Check whether a string is empty.
10. Trim leading, trailing, or extra spaces from a string.
11. Get the character at a given index.
12. Get the Unicode code point of a character at an index.
13. Get the Unicode code point before a given index.
14. Find the first occurrence of a character in a string.
15. Find the last occurrence of a character in a string.
'''
'''
# 1. Find the length of a string.
s = input('Enter The string: ')
print(len(s))


#2. Copy one string to another.
s = input('Enter The string: ')
s1 = s
print(s1)


#3. Concatenate two strings.
s1 =input('Enter first string: ')
s2 =input('Enter second string: ')
print(f'{s1+s2}')
'''
'''
#4. Compare two strings (case-sensitive).
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if s1 == s2:
    print('equal')
else:
    print('not equal')

#5. Compare two strings ignoring case.
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if s1.lower() == s2.lower():
   print('equal')
else:
    print('not equal')

'''
'''
#6. Convert a string to uppercase.
s = input('Enter the string: ')
print(s.upper()) 


#7. Convert a string to lowercase.
s = input('Enter the string: ')
print(s.lower()) 


#8. Toggle the case of each character in a string.
s = input('Enter the string: ')
print(s.swapcase()) 
'''

'''
#9. Check whether a string is empty.
s1 = input("Enter the string: ")

if s1 == '':
   print('True')
else :
   print('False')
'''

'''
#10. Trim leading, trailing, or extra spaces from a string.
s1 = input("Enter the string: ")
print(s1.strip())

'''

'''
#11. Get the character at a given index.
s1 = input("Enter the string: ")
In = input("Enter the Index: ")  

for i in range(len(s1)):
   if i == int(In):
      print(s1[i])
'''
'''
#12. Get the Unicode code point of a character at an index.
s1 = input("Enter the string: ")
In = input("Enter the Index: ")  

for i in range(len(s1)):
   if i == int(In):
      print(ord(s1[i]))
'''
'''
#13. Get the Unicode code point before a given index.
s1 = input("Enter the string: ")
In = input("Enter the Index: ")  

for i in range(len(s1)):
   if i == int(In)-1:
      print(ord(s1[i]))
'''

'''
#14. Find the first occurrence of a character in a string.
s1 = input("Enter the string: ")
Char = input("Enter the Char: ")  

for i in range(len(s1)):
   if s1[i] == Char:
      print(i)
      break
'''
#15. Find the last occurrence of a character in a string.
s1 = input("Enter the string: ")
Char = input("Enter the Char: ")  

for i in range(len(s1)-1,0,-1):
   if s1[i] == Char:
      print(i)
      break 
      


