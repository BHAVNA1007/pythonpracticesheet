'''
5. Equilibrium Index Finder
===========================

Scenario

Find an index where:

# Sum of elements on the left side

Sum of elements on the right side

Requirements

* Read N and list elements from user
* Find equilibrium index
* If not found, display message

Test Case 1

Input:
[1, 3, 5, 2, 2]

Output:
Equilibrium Index = 2

Explanation:
1 + 3 = 2 + 2

Test Case 2

Input:
[1, 2, 3]

Output:
No Equilibrium Index Found
'''

n = int(input("Enter size: "))
print("enter ele...")
arr = []
for i in range(n):
    arr.append(int(input(f"ele {i+1} is :")))
print(arr)

found = 0

for k in range(n):
   l_s = 0
   r_s = 0

   for i in range(k): #k=(len(arr)//2)
      l_s += arr[i]
   

   for i in range(k+1,n): #k=(len(arr)//2)
      r_s += arr[i] 
  

   if l_s == r_s:
      print("Equilibrium Index = ", k ) #k=(len(arr)//2)
      found = 1
      break

if found == 0:
   print("No Equilibrium Index Found")

    





