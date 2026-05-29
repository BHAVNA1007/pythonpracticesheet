'''
1.Student Marks Management
Create a program to store student marks in a List and perform operations.

Requirements:

Add student marks into a List
Display all marks
Find highest and lowest marks
Count students who scored above 75

Test Cases:

Input: [45, 67, 89, 90, 76] → Highest = 90, Lowest = 45, Count Above 75 = 3
Input: [10, 20, 30] → Highest = 30, Lowest = 10, Count Above 75 = 0
Input: [100, 99, 98] → Highest = 100, Lowest = 98, Count Above 75 = 3
'''
n = int(input('Enter the size of list: '))

print('Plz enter the marks...')

marks = []

i =0
while i < n:
   x = int(input('Element: '))
   marks.append(x)
   i += 1
print(marks)

max = marks[0]
for i in range(1,n):
   if marks[i]>max:
      max = marks[i]
print('Highest =', max)

min = marks[0]
for i in range(1,n):
   if marks[i]<min:
      min = marks[i]
print('Lowest =', min)

count = 0
for i in range(n):
   if marks[i]>75:
      count += 1
print('Count Above 75=', count)




