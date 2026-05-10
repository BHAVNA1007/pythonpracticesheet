'''
5.Tech Number Checker

A number is called a Tech Number if:

It has even number of digits
Split it into two equal halves
Add both halves
Square the sum
If result equals original number → Tech Number

Write a program to:

Count digits
If digits are even, split the number
Find sum of both halves
Square the sum
Display intermediate values
Check and print result

Input:
2025

Output:
First Half = 20
Second Half = 25
Sum = 45
Square = 2025
Tech Number
'''
num = input("Enter The Number = ")
l = len(num)
f_h =""
s_h =""
sum = 0
for i in range(l//2):
     f_h +=str(num[i]) 

for i in range(l//2,l):
     s_h +=str(num[i])

sum = int(f_h) + int(s_h)

square = sum**2

print("First Half = ",f_h)
print("Second Half = ",s_h)
print("Sum = ",sum)
print("Square = ",square)

if int(num) == square:
    print("Tech Number")
else:
    print("Non Tech Number")
    