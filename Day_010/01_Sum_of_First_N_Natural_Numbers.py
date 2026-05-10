'''
1. Sum of First N Natural Numbers
A teacher wants to reward students by giving points daily. On day 1, a student gets 1 point, day 2 → 2 points, and so on. This follows a natural number sequence.
Write a program to calculate the *total points earned after n days* by summing all natural numbers up to n using loops.

Input: n = 10
Output: Total Points = 55

n = int(input("Enter a number = "))
x = 1
sum = 0

while x <= n:
   sum += x
   x += 1
print("Total points = ", sum)
'''

n = int(input("Enter a number = "))
sum = 0
for i in range(n+1):
    sum += i
print("Total Points = ", sum)



