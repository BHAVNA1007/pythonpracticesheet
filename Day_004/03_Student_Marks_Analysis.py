'''Assignment 3: Student Marks Analysis

A student wants to calculate total marks, average, and percentage from 5 subjects.

Input:
Marks = 78, 85, 90, 88, 80

Expected Output:
Total = 421
Average = 84.2
Percentage = 84.2
'''

sub1,sub2,sub3,sub4,sub5 = map(int,input().split())
print(f"Marks = {sub1}, {sub2}, {sub3}, {sub4}, {sub5}")
total = sub1+sub2+sub3+sub4+sub5
print(f"Total = {total}")
avg = total/5
print(f"Average = {avg}")
persentage = (total/500)*100
print(f"Percentage ={persentage }")
