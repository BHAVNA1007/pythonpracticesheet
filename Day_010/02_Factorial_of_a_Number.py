'''
2. Factorial of a Number
In project scheduling, tasks are dependent on previous tasks, and the total number of ways to arrange them is calculated using factorial. Factorial of a number n is the product of all numbers from 1 to n.
Write a program to calculate the *factorial of a given number using loops*.

Input: n = 5
Output: Total Ways = 120

n = int(input("Enter a number = "))
x = 1
fact = 1
while x<=n:
  fact = fact * x 
  x += 1
print("Total ways = ",fact)
'''
n =  int(input("Enter a number = "))

fact = 1
for x in range(1,n+1):
     fact = fact * x
  
print("Total Ways = ",fact)
