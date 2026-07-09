'''
22 3Sum Closest

Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 '''


n = int(input("Enter N: "))    

nums = []

for i in range(n):
   nums.append(int(input(f"Ele {i+1}: ")))
print(nums)

target = int(input("target: "))

closest = nums[0] + nums[1] + nums[2]

for i in range(n):
  
   for j in range(i+1, n):

      for k in range(j+1, n):
         curr_sum = nums[i] + nums[j] + nums[k]
         if abs(target - curr_sum) < abs(target - closest):
     
             closest = curr_sum

print(closest)
 
           

           