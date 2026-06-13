'''
15 Third Maximum Number
Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
 '''
n = int(input("Enter size of arry: "))
nums = []
for i in range(n):
    nums.append(int(input()))
print(nums)    

g = nums[0]
for i in range(n):
    if len(nums) < 3:
        if nums[i] > g:
            g = nums[i]
            print(g)
        
        
                    