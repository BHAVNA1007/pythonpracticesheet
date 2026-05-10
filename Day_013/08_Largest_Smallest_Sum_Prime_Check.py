'''8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime
'''

import math
num = int(input("Enter a number = "))

l_num = 0
s_num = 9

while num > 0:
    digit = num % 10
    if l_num < digit:
        l_num = digit
    else:
        if s_num > digit:
            s_num = digit
    num = num // 10
print("Largest = ", l_num)
print("Smallest = ", s_num)

sum = l_num + s_num
print("Sum = ", sum)

if sum <= 1:
    print("not prime")
else:
    x = 0
    i = 2
    while i <= math.sqrt(sum):
        if sum % i == 0:
           x = 1
           break
        i += 1
    if x == 0:
        print("Prime ")
    else:
        print("Not Prime ")
 