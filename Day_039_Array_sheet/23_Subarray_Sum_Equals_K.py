'''
23 Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
 '''

n = int(input("Enter n: "))

nums = []

for i in range(n):
   nums.append(int(input(f"elements {i+1} : ")))
 
print(nums)

target = int(input("Enter k : "))
count = 0
for i in range(n):

    for j in range(i,n):
 
        sum = 0
        for k in range(i,j+1):
            sum = sum + nums[k]
        if sum == target :
               count += 1

print(count)
  
  
        