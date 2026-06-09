'''
6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to *check whether a number is an Armstrong number using loops*.

Input: 153
Output: Armstrong
'''
num = int(input("Enter a number = "))
l = len(str(num))
sum = 0
new_num = num
while num > 0:
    digit = num % 10
    sum = sum + digit ** l
   
    num = num // 10
   
if sum == new_num:
    print("Armstrong number")
else:
    print("not a Armstrong number")
    