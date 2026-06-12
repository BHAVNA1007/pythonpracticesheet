'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''
n = int(input("Enter size of array: "))
 
nums = []
for i in range(n):
     nums.append(int(input()))
print(nums)    

zeros = []
num = []

for i in nums:
    if i > 0:
        num.append(i)
    else:
        zeros.append(i)       
        
print(zeros)
print(num)    

new =  num + zeros 
print(new)
    
        
     