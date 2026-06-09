'''
5.Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code
'''
code = input('Enter product code: ')
n = len(code)
res=''
for i in range(n-1,-1,-1):
    ch = code[i]
    res = res + ch
print(res) 
    
if res==code:
   print('Palindrome Code')

else:
   print('Not a Palindrome Code') 
    