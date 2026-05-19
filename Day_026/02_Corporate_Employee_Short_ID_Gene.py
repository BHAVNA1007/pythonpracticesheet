'''
02_Corporate_Employee_Short_ID_Generator

A multinational company wants to automatically generate short IDs for
employees while creating official email accounts. The system should take
the employee’s full name and create an ID using the first character of
each word.

Conditions: - Take first character of every word - Convert all
characters to uppercase

Input: Enter employee name: ajay singh thakur

Output: Employee Short ID: AST
'''
e_name = input('Enter employee name: ')

s = e_name.split()

i=0
short_id = ''
while i< len(s):
   word = s[i]
   ch = word[0]

   if ch>='a' and ch<='z':
       ch = chr(ord(ch)-32)

   short_id += ch
   i += 1

print('Employee Short ID: ',short_id)   
    