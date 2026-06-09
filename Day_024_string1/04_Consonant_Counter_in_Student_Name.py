'''
4.Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 11

'''

s_name = input("Enter student name: ").lower()
count = 0


for ch in s_name:
   if ch>="a" and ch<="z":
     if ch != 'a' and  ch != 'e' and ch != 'i' and ch != 'o' and ch != 'u' : 

         count += 1

print("Total consonants: ", count)