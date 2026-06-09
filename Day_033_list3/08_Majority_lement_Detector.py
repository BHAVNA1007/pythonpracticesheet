'''
8. Majority Element Detector
============================

Scenario

Find an element occurring more than N/2 times.

Requirements

* Read N and list elements from user
* Find majority element
* If not present, display appropriate message

Test Case 1

Input:
[2, 2, 1, 2, 3, 2, 2]

Output:
Majority Element = 2

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Majority Element Found
'''
n = int(input("Enter size: "))
print("enter ele...")

arr = []
for i in range(n):
    arr.append(int(input(f"ele {i+1} is :")))
print("Array = ",arr)

found = 0


for i in arr:
   count = 0
   for j in arr:
       if i == j:
          count += 1

   if count > n//2:
      found = 1
      res = i 
      break  
         
if found == 1:
   print("Majority Element =", res)
else:
   print("No Majority Element Found")
            
   