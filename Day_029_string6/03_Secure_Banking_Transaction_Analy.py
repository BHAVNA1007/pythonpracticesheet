'''
03_Secure_Banking_Transaction_Analyzer

A banking server generates encrypted transaction IDs using letters and digits.

The fraud detection team wants a Python program to find the first digit that does not repeat in the transaction ID.

If no unique digit exists, print:

text
No unique digit found

### Input:
text
A122334455667789

### Output:
text
8
'''
s = input('Enter the string: ')


for i in range(len(s)):

    count = 0

    for j in range(len(s)):
       if s[i] == s[j]:
           count += 1

          
    if count == 1:
       print(s[i])
       break

else:
   print("No unique digit found")
        


