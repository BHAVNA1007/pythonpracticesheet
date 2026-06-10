'''
7 Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]

Output: 4

Example 3:
Input: nums = [1]
Output: 1
'''
n = int(input("Enter size of array: "))
nums = []
for i in range(n):
    nums.append(int(input()))
print(nums)    


for i in nums:
    unique = 0
    for j in nums:
        if i == j:
            unique += 1
            break
    if unique == 1:
        print(i)
        break
        
    