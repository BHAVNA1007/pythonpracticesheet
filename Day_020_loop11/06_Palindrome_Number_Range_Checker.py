'''
6.Palindrome Number Range Checker

A barcode verification system checks for palindrome numbers within a specific range.
The user enters starting and ending numbers.
The system displays all palindrome numbers using nested loops.

Input:
Enter starting number: 100
Enter ending number: 200

Output:
Palindrome Numbers are:
101
111
121
131
141
151
161
171
181
191
'''
s = int(input("Enter starting number ="))
e = int(input("Enter ending number = "))

for n in range(s, e+1):
   temp = n

   rev = 0
   while temp > 0:
       digit = temp % 10
       rev = rev*10 + digit
       temp = temp // 10
   if rev == n:
      print(n)    

       
   