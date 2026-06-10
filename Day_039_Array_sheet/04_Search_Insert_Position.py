'''
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 '''
n = int(input("Enter size of array: "))
 
nums = []
for i in range(n):
   nums.append(int(input()))
nums.sort()    
print("nums = ", nums)

target = int(input("target = "))


for i in range(len(nums)):
    if nums[i] >= target:
        print(i) 
        break        
else:
        print(len(nums))                
                

    