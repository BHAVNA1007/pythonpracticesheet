'''5. Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3
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
        print("Next Prime ID =", next_prime)
        break

    next_prime += 1

diff = abs(num - next_prime )
print("Gap = ", diff)
'''




import math
num = int(input("Enter The Number = "))

n_prime = num + 1

while True:
     
     if n_prime <= 1:
         print("Not Prime ")
     else:
         for i in range(2, int(math.sqrt(n_prime)+1)):
              if n_prime % i == 0:
                 break
         else:
             print("Next Prime = ", n_prime)
             break
     n_prime += 1  


gap = abs(num - n_prime)
print("Gap = ", gap)
             






