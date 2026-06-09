'''
10. Student ID Validity Checker (Count Odd Digits)
A school management system assigns numeric IDs to students. The administration wants to verify IDs by checking how many odd digits are present in each ID number. IDs with more odd digits are sent for manual review.

Write a program to count the number of odd digits in a given student ID using loops.

Input:
572943

Output:
Odd Digits Count = 3
'''
number = int(input())

count = 0

while number > 0:
    digit = number % 10
    if digit % 2 != 0:
       count += 1
    number = number // 10
print("Odd Digits Count = ",count)