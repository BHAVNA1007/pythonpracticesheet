'''
6.Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching
'''
p1 = input('Enter first string: ')
p2 = input('Enter second string: ')

s1=''
s2=''

for ch in p1:
   if ch != ' ':
      if ch >= 'A' and ch <= 'Z':
           ch = chr(ord(ch)+32)
      s1 = s1 + ch

for ch in p2:
   if ch != ' ':
      if ch >= 'A' and ch <= 'Z':
         ch = chr(ord(ch)+32)
      s2 = s2 + ch
  
if len(s1) == len(s2):
   match = True
  
   for ch in s1:
       c1 = 0
       c2 = 0

       for i in s1:
          if i == ch:
              c1 += 1
       for j in s2:
          if j == ch:
              c2 += 1
       if c1 != c2:
          match = False
          break
   if match:
        print("Both Product Codes are Matching")

   else:
        print("Both Product Codes are Not Matching")

else:
    print("Both Product Codes are Not Matching")
   

