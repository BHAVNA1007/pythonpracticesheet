'''
1.Second Largest Unique Number
Scenario

A sports academy stores athlete scores in a list.

Find the second largest unique score.

Requirements
Read N and list elements from user
Find second largest unique number
If not available, display a message
Test Case

Input:

[10, 20, 30, 40, 40]

Output:

Second Largest = 30
'''

n = int(input('Enter a size of arr: '))

arr = []
for i in range(n):
   arr.append(int(input(f"enter ele {i+1}: ")))
print(arr)

unique = []

for i in arr:
    if i not in unique:
       unique.append(i)

unique.sort()
print(unique)    

print("Second Largest = ",unique[-2]) 

 
    













