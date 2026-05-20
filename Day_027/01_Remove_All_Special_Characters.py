'''
01_Remove_All_Special_Characters_from_a_String

Online Banking Customer Data Cleaning System

A private bank has launched a new online account opening portal. While entering customer details, many users accidentally type unnecessary symbols, emojis, hashtags, dollar signs, and special characters in their names and addresses.

Before storing the data into the database, the bank wants a Python program that removes all unwanted special characters and keeps only:

* Alphabets
* Numbers
* Spaces

The cleaned value should be stored back into the original string variable.

Input:

Deepika@@ Padukone!! 123
Output:
Deepika Padukone 123
Input:
Ajay###Singh$$$
Output:
AjaySingh
'''
name_add =input('Enter the string: ')

i = 0 
clean = ''
 
while i < len(name_add):
   ch = name_add[i]
   if (ch<='z' and ch>='a') or (ch>='A' and ch<='Z') or (ch>='0' and ch<='9') or ch==" ":
       
       clean += ch
  
   i += 1

original = clean
print("update in orignal string ",original)









