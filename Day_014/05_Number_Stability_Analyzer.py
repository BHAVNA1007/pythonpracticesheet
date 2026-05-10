'''5.Number Stability Analyzer

A science lab studies whether digits are in increasing order.

Write a program using for-else loop:

- If every next digit is greater than previous print Stable Number
- Else Unstable Number

Input:
12359

Output:
Stable Number
'''

num = int(input("Enter a number = "))

l = len(str(num))

for i in range(l-1):
    d1 = num // 10 ** (l-i-1) % 10
    d2 = num // 10 ** (l-i-2) % 10
    

    if d2 <= d1:
        print("Unstable Number")
        break
        
else:
     print("stable Number")
     