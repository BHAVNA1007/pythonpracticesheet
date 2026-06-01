'''
7. Array Rotation Analyzer
==========================

Scenario

Rotate the array K times towards the right.

Requirements

* Read N and list elements from user
* Read K
* Rotate the array
* Display rotated array

Test Case 1

Input:
Array = [1, 2, 3, 4, 5]
K = 2

Output:
[4, 5, 1, 2, 3]

Test Case 2

Input:
Array = [10, 20, 30, 40]
K = 1

Output:
[40, 10, 20, 30]
'''

n = int(input("Enter size: "))
print("enter ele...")

arr = []
for i in range(n):
    arr.append(int(input(f"ele {i+1} is :")))
print("Array = ",arr)
k = int(input("K = "))

last = arr[n-k:]


i = n - k -1

while i >= 0:
    arr[i+k] = arr[i]
    i = i - 1

for i in range(k):
    arr[i] = last[i]
print(arr) 


