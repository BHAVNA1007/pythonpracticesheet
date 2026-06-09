'''
2. Smallest Digit in Number
A manufacturing company prints serial numbers on products. During quality testing, the scanner needs to detect the smallest digit in the serial number to verify coding standards.
Write a program to find the smallest digit in a number using loops.

Input:
57294

Output:
Smallest Digit = 2
'''
'''
num = int(input("Enter a number = "))
s_num = 9

while num > 0:
    l_digit = num % 10
    if l_digit < s_num:
        s_num = l_digit
    num = num // 10
print("Smallest Digit = ",s_num) 
