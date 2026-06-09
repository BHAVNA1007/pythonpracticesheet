'''7.
 Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number
'''
'''
import math

num = int(input('Enter a number = '))

sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10
print("Sum = ", sum)

if sum <= 1:
    print("Normal Number")

else:
    x = 0
    i = 2
    while sum <= math.sqrt(sum):
        if sum % i == 0:
            x = 1
            break
        i += 1
    if x == 0:
        print("Lucky Number") 
    else:
        print("Normal Number")  
'''
import math
num = input("Enter The Number = ")
sum = 0

for digit in num:
    sum += int(digit)
print("Sum = ", sum)  

prime = True
if sum <= 1:
    prime = True
    print("Not Prime")
else:
    for i in range(2, int(math.sqrt(sum))):
        if sum % i == 0:
            prime = False
            print("Not prime ")
            break
    else:
        print("Prime")



