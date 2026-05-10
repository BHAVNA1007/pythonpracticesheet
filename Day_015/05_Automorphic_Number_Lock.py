'''5_Automorphic_Number_Lock

A high-security digital locker validates access codes using a special mathematical rule.

When a user enters a numeric code, the system squares the number and checks whether the last digits of the square match the original number.
 If it matches, the code is considered valid.

An Automorphic Number is a number whose square ends with the same number.

Task:
Write a Python program to check whether a given number is an Automorphic Number or not.

Example:
Input:
25

Output:
Automorphic Number
'''

n = int(input("Enter a number = "))

new = n

same_num = False
square = n**2
while new > 0:
    if new % 10 == square % 10:
        same_num = True

    square= square // 10
    new = new // 10
if same_num:
    print("Automorphic Number")
else:
    print("Not Automorphic Number")