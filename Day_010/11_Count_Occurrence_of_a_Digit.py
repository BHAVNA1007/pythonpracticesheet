'''
*11. Count Occurrence of a Digit*
A system logs repeated digits in a number for pattern analysis and reporting.
Write a program to *count how many times a given digit appears in a number using loops*.

Input: Number = 122312, Digit = 2
Output: 3
'''
num = input("Number = ")
digit = input("Digit = ")

count = 0

for i in num:
   if digit == i:
      count += 1
print(count)
   