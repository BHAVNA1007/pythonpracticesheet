'''
2. Digit Sum Mirror Checker

A validation system checks symmetry in digit sums.

Write a program to:

Split number into two halves
Find sum of first half digits
Find sum of second half digits
Display both sums
If both sums are equal → print Balanced Number
Else → print Unbalanced Number

Input:
123321

Output:
First Half Sum = 6
Second Half Sum = 6
Balanced Number
'''
num = input("Enter The Number = ")
l = len(str(num))
sum1 = 0
sum2 = 0
for i in range(l//2):
    sum1 += int(num[i])

for i in range(l//2, l):
    sum2 += int(num[i])
    
print("First Half Sum = ",sum1)
print("Second Half Sum =",sum2)

if sum1 == sum2:
   print("Balanced Number")
else:
   print("Unbalanced Number")
