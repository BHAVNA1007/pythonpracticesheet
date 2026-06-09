'''2. Next Prime ID Generator

A multinational company auto-generates employee IDs in numeric sequence.
 Due to internal policy, only prime numbered IDs are assigned to new premium employees.

The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

Write a program to find the first prime number after n.

Input:
14

Output:
Next Prime = 17
'''
'''
import math

num = int(input("Enter a number = "))

next_prime = num + 1   
while True:
    x = 0

    if next_prime <= 1:
        x = 1
    else:
        i = 2
        while i <= math.sqrt(next_prime):
            if next_prime % i == 0:
                x = 1
                break
            i += 1

    if x == 0:
        print("Next Prime =", next_prime)
        break

    next_prime += 1
'''

import math

num = int(input("Enter The Number = "))

next_prime = num + 1

while True:
    
    

    if next_prime <= 1:
       print("Not Prime")

    else:
       for i in range(2, int(math.sqrt(next_prime)+1)):
            if next_prime % i == 0:
                break
       else:
            print("Next Prime",next_prime) 
            break
    next_prime += 1  


