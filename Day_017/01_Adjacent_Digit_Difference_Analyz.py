'''
1. Adjacent Digit Difference Analyzer

A system analyzes differences between consecutive digits in a number.

Write a program to:

Find the difference between every pair of adjacent digits
Display all differences
Count how many differences are even
Find the largest difference
If all differences are same → print Uniform Difference
Else → print Non-Uniform Pattern

Input:
84261

Output:
Differences: 4 2 4 5
Even Differences Count = 3
Max Difference = 5
Non-Uniform Pattern
'''

num = int(input("Enter The Number = "))
l = len(str(num))
print("Differences:", end=" ")
count = 0
max = 0
st = " "
while l > 1:
     
     d1 = num//10**(l -1)%10
     d2 = num//10**(l -2)%10
     diff = abs(d1-d2)
     st += str(diff)
     print(diff,end=" ")
     l -= 1
     if diff % 2 == 0:
         count += 1 
              
     if max < diff:
         max = diff
print("\nEven Differences Count = ",count)
print("Max Difference = ",max)

Uniform = False
for i in range(len(st) - 1):
    if st[i] == st[i + 1]:  
       Uniform = True
    else:
       Uniform = False

if Uniform:
    print("Uniform Difference")
else:
    print("Not Uniform Difference")


