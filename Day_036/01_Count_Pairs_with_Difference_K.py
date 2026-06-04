'''
1. Count Pairs with Difference K

A company records the ages of employees. Find how many pairs of employees have an age difference exactly equal to K.

Problem Statement:

Given an array of employee ages and an integer K, count the number of pairs whose absolute difference is K.

Example:

Input:

N = 5
K = 2
ages[] = {1, 5, 3, 4, 2}

Output:

3

Explanation:

(1,3), (3,5), (2,4)
'''

n = int(input("Enter size N: "))
k = int(input("Enter k: "))

arr = []
for i in range(n):
  arr.append(int(input(f"ele..{i+1}: ")))
print(arr)

count  = 0
for i in range(len(arr)):
    for j in range(len(arr)):
         diff = abs(arr[i]) - abs(arr[j])

         if diff == k:
            print(f"{arr[i],arr[j]}")
            count += 1
print(count)
            
            



  
