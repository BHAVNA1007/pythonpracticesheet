'''
9 Intersection of Two Arrays II

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 
'''

n = int(input("Enter size of arr1: "))
nums1 = []
for i in range(n):
    nums1.append(int(input()))
print(nums1)    

n2 = int(input("Enter size of arr2: "))
nums2 = []
for i in range(n2):
    nums2.append(int(input()))
print(nums2)

res = []
for i in nums1:
    if i in nums2:
        res.append(i)
print(res)            
            
            
    