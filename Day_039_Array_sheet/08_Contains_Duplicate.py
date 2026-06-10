'''
8 Contains Duplicate
Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true
'''

n = int(input("Enter size of array: "))
nums = []
for i in range(n):
    nums.append(int(input()))
print(nums)    

duplicate = False
for i in nums:
    count = 0
    for j in nums:
        if i == j:
            count +=1
            
    if count > 1 :
        duplicate = True 
        break        
print(duplicate)        
        
        
        
    