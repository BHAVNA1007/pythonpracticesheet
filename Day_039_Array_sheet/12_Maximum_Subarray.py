'''
12 Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.

 Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

'''
'''
n = int(input("Enter size n: "))

nums = []
for i in range(n):
    nums.append(int(input(f"ele {i+1}: ")))

print(nums)

max_sum = float('-inf')

for i in range(n):

    for j in range(i, n):

       sum = 0
       for k in range(i, j+1):
          sum += nums[k]

       if sum > max_sum:
          max_sum = sum

print(max_sum) 

'''

# time com o(n)^3 


#better o(n)^2

n = int(input("Enter size: "))
nums = []

for i in range(n):
   nums.append(int(input(f"Ele {i+1}: ")))
print(nums)

max_sum = float('-inf')

for i in range(n):
    
    sum = 0
    for j in range(i, n):
    
        sum += nums[j]

        if sum > max_sum:
           max_sum = sum

print(max_sum)

             
            
       
  


