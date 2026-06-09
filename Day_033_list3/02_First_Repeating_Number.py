'''
2. First Repeating Number
=========================

Scenario

A security system logs employee IDs.

Find the first ID that repeats in the list.

Requirements

* Read N and list elements from user
* Find the first repeating number
* If no repeating number exists, display an appropriate message

Test Case 1

Input:
[10, 5, 3, 4, 3, 5]

Output:
First Repeating Number = 3

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Repeating Number Found

'''

n = int(input("Enter the size: "))
print("plz enter elements...")

v_ids = []
for i in range(n):
    v_ids.append(int(input("id: ")))
print(v_ids)

found = 0
for i in range(len(v_ids)):
    count = 0
    for j in range(0,i+1):
        if v_ids[i] == v_ids[j]:
            count += 1
            
    if count > 1:
       print("First Repeating Number = ",v_ids[i])
       found = v_ids[i]
       break

if found == 0:
    print("No Repeating Number Found")  
      


