'''
4. Digit Gap Consistency Checker

A number analysis system checks whether the gap between digits follows a consistent pattern.

Write a program to:

Find the absolute difference between first two digits
Compare this difference with all next adjacent digit differences
If any difference is not equal to the first difference, stop using break
Display:
- Initial gap
- Whether all gaps are same or not

Input:
8642

Output:
Initial Gap = 2
Consistent Pattern

Input:
97531

Output:
Initial Gap = 2
Consistent Pattern

Input:
5321

Output:
Initial Gap = 2
Pattern Break Detected
'''
num = input('Enter The Number = ')
l = len(num)
consistent = True
first_gap = abs(int(num[0])- int(num[1]))
for i in range(1, l-1):
   d1 = int(num[i])
   d2 = int(num[i+1])
   diff = abs(d1 - d2)
   
   if first_gap != diff:
      consistent = False
      break
print("Initial Gap = ", first_gap)
if consistent:
    print("Consistent Pattern")
else:
    print("Pattern Break Detected") 
