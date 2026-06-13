'''
14 Find the Difference of Two Arrays
Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums1. Therefore, answer[1] = [4,6].
Example 2:

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
'''
n1 = int(input("Enter a size of arr1: "))

nums1 = []
for i in range(n1):
    nums1.append(int(input()))
print(nums1)


n2 = int(input("Enter a size of arr2: ")) 
nums2 = [] 
for i in range(n2):
    nums2.append(int(input())) 
print(nums2)    

nu1 = []
for i in nums1:
    if i not in nums2:
        if i not in nu1:
            nu1.append(i)
#print(nu1)    
    
nu2 = []
for i in nums2:
    if i not in nums1:
        nu2.append(i)   
#print(nu2)   

res = list([nu1,nu2])     
print(res)
        
        
        
        


    