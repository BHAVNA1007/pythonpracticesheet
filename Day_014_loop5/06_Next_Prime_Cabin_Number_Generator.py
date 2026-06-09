'''6.
Next Prime Cabin Number Generator

A luxury hotel gives only prime numbered cabins to VIP guests.

Manager enters the last allotted cabin number.
System must find the next available prime cabin number.

Write a program using loops.

Input:
24

Output:
Next Prime Cabin = 29
'''
import math
num = int(input("Enter the number = "))

n_p = num+1


while True :
    if n_p <= 1:
        print("Not Prime")
    else:
        for i in range(2, int(math.sqrt(n_p))):
             if n_p % i == 0:
                 print("Not Prime") 
                 break
        else:
            print("Next Prime Cabin", n_p)
            break
    n_p += 1