'''
1. First Non-Repeating Number
   ====================================================================

Scenario

An online voting system stores vote IDs in a list.

Find the first vote ID that appears only once.

Requirements

* Read N and list elements from user
* Find the first non-repeating number
* If no such number exists, display an appropriate message

Test Case 1

Input:
[4, 5, 1, 2, 1, 2, 4]

Output:
First Non-Repeating Number = 5

Test Case 2

Input:
[7, 7, 8, 8]

Output:
No Non-Repeating Number Found
'''
n = int(input("Enter the size: "))
print("plz enter elements...")

vote_ids = []
for i in range(n):
    vote_ids.append(int(input(f'vote_id : ')))
print(vote_ids)

v_id = 0
for i in vote_ids:
    count = 0
    for j in vote_ids:
       if i == j:
           count += 1
    if count == 1:
       print("First Non-Repeating Number =", i ) 
       v_id = 1
       break
if v_id == 0:
     print("no Non-Repeating Number")
      
