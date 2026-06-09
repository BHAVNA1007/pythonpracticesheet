'''
2.Student Pass List Generator (Using List Comprehension)

A school stores student marks in a list. Generate a new list containing only the marks of students who have passed (marks ≥ 40).

Requirements
Read N and marks from user
Use List Comprehension
Create Pass List
Display Pass Count
Test Case

Input:

[25, 40, 55, 78, 30, 90]

Output:

Pass List = [40, 55, 78, 90]
Pass Count = 4
'''

n = int(input("Enter n: "))

marks = []
for i in range(n):
   marks.append(int(input("marks: ")))
print(marks)

count = 0
pass_list = [i for i in marks if i >= 40 ]
print(pass_list)

count_pass = len(pass_list)
print("Pass Count: ",count_pass)










