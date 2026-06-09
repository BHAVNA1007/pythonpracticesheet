'''8.
Mirror Difference Transaction Verification System
A multinational banking company processes thousands of daily transaction IDs. To detect suspicious patterns and validate system-generated IDs,
 the security software performs a Mirror Difference Verification Test.
For every entered transaction ID:

Reverse the digits of the transaction ID

Find the absolute difference between the original ID and the reversed ID

Count the total number of digits in the difference

Apply the following conditions using if-elif-else:

If the difference is 0, print Perfect Match

Else if the difference is divisible by 9, print Verified

Else print Rejected

Write a program to automate this verification process using loops and conditional statements.
Input:
4215
Output:
Reverse = 5124Difference = 909Digits = 3Verified
Input:
1221
Output:
Reverse = 1221Difference = 0Digits = 1Perfect Match
Input:
1234
Output:
Reverse = 4321Difference = 3087Digits = 4Verified
'''
num = int(input("Enter a number = "))
rev = 0
new_num = num 
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
print("Reverse = ", rev)

if new_num > rev:
     diff = new_num - rev
     print("Difference = ", diff)
else:
     diff =  rev - new_num 
     print("Difference = ", diff)


new_diff = diff
count = 0
if diff == 0:
   print("Digits = ",count+1)
else:
    while diff > 0:
    
       digit = diff % 10
       count += 1
       diff = diff // 10
    print("Digits = ",count)


if new_diff == 0:
     print("Perfect Match")
elif new_diff % 9 == 0:
     print("Verified")
else:
     print("Rejected")

