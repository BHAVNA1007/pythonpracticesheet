'''
3. Missing Number Detector
==========================

Scenario

Numbers from 1 to N should exist in a sequence, but one number is missing.

Requirements

* Read N and list elements from user
* Find the missing number
* Assume numbers belong to the range 1 to N+1

Test Case 1

Input:
[1, 2, 3, 5]

Output:
Missing Number = 4

Test Case 2

Input:
[2, 3, 4, 5]

Output:
Missing Number = 1
'''

n = int(input("Enter size: "))
print("enter ele...")
arr = []
for i in range(n):
    arr.append(int(input(f"ele {i+1} is :")))
print(arr)

for i in range(1,n+2):
   if i in arr:
       continue
   else:
       print("Missing Number =",i) 








