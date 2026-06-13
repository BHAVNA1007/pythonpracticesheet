'''
25 Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
'''

n = int(input("Enter the size of arr:  "))

nums = []
for i in range(n):
    nums.append(int(input()))
print(nums)

f_index = -1
l_index = -1

target = int(input("Enter target: "))
for i in range(n):
    if nums[i] == target:
        if f_index == -1:
            f_index = i
            
        l_index = i          
print([f_index, l_index])        
    
