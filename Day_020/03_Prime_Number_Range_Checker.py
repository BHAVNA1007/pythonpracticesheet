'''
3.Prime Number Range Checker

A cyber security system generates prime numbers for encryption analysis.
The user enters a starting number and ending number.
The system checks and displays all prime numbers between the given range using nested loops.

Input:
Enter starting number: 10
Enter ending number: 50

Output:
Prime Numbers are:
11
13
17
19
23
29
31
37
41
43
47
'''
import math
s = int(input("Enter starting number: "))
e = int(input("Enter ending number: "))

for n in range(s,e+1):
    x = 1
    i = 1
    if n > 1:
       i = 2
       
       while i <= int(math.sqrt(n)):
           if n % i == 0:
              break
           i += 1 
       else:
           print(n)
    x += 1
     
       
        








