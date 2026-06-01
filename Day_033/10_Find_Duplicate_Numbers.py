'''
10. Find Duplicate Numbers
==========================

Scenario

A company stores employee IDs in a list. Some IDs may appear more than once due to data entry errors.

Requirements

* Read N and list elements from user
* Find all duplicate numbers
* Store duplicates in another list
* Count total duplicate numbers
* Display duplicates in sorted order

Test Case 1

Input:
[1, 2, 3, 2, 4, 5, 1]

Output:
Duplicate Numbers = [1, 2]
Count = 2

Test Case 2

Input:
[10, 20, 30]

Output:
No Duplicate Numbers Found
'''

n = int(input("Enter size: "))
print("enter ele...")
arr = []
for i in range(n):
    arr.append(int(input(f"ele {i+1} is :")))
print(arr)


r_count = 0
dup = []
for i in arr:
    count = 0
    for j in arr:
        if i == j:
           count += 1
    if count > 1:
       if i not in dup:
          r_count += 1
          dup.append(i) 

dup.sort()

if dup == []:
   print("no duplicate") 

else:
   print("Duplicate Numbers = ", dup)
   print("Count: ",r_count)  
     
    
  
     







