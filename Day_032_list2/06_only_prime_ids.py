'''
6.A security system logs employee entry IDs during a day.

Only prime-numbered IDs are considered valid VIP entries.

Tasks:

Extract all prime IDs from the list
Find the sum of prime IDs
Find the maximum prime ID
Count how many prime entries exist

Input:
A list of integers (may contain duplicates and non-prime numbers)

Example 1

Input:
[12, 5, 7, 9, 11, 14, 17]

Output:
Prime IDs = [5, 7, 11, 17]
Sum = 40
Max = 17
Count = 4

Example 2

Input:
[4, 6, 8, 10]

Output:
Prime IDs = []
Sum = 0
Max = -1
Count = 0
'''

n = int(input('Enter the size: '))
print("plz enter ele...")

arr = []
for i in range(n):
    arr.append(int(input()))
print(arr)

prime = []

for num in arr:
   if num > 1:
      is_prm = True
      
      for i in range(2,num):
           if num % i == 0:
              is_prm = False
              break  
      if is_prm:
          prime.append(num)   
print("Prime IDs = ",prime)

sum = 0
for i in prime:
    sum += i
print("Sum: ",sum)

max = prime[0]
for i in range(1,len(prime)):
    if prime[i] > max:
        max = prime[i]
print("Max: ", max)

print("Count: ", len(prime))

      
       
          
       















