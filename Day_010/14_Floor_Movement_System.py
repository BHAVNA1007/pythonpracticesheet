'''
14.Floor Movement System (Elevator)
An elevator system takes the current floor and destination floor as input.

If current floor < destination → move upward and display floors
If current floor > destination → move downward and display floors
If both are same → display "Already on the same floor"

Write a program using if-elif-else and loops to simulate elevator movement.

Input: 1, 5
Output: 1 → 2 → 3 → 4 → 5

Input: 7, 3
Output: 7 → 6 → 5 → 4 → 3

Input: 4, 4
Output: Already on the same floor
'''
curr_floor,dest = map(int,input().split())

if curr_floor < dest:
       for i in range(curr_floor,dest+1):
           print(i, end="->")
else:
    if curr_floor > dest:
        for i in range(curr_floor,dest-1,-1):
           print(i, end="->")
    else:
        if curr_floor == dest:
             print("Already on the same floor")
       

  
