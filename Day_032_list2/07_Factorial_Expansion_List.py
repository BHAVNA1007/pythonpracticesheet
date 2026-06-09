'''
7.Factory Production – Factorial Expansion List

Problem Statement

A factory produces items where production capacity is defined using factorial growth.

Given a list of numbers, replace each number with its factorial value.

Then perform analysis on the resulting list.

Tasks:

Convert each element to factorial
Find sum of all factorial values
Find maximum factorial value
Count how many factorial values are even

Input:
A list of integers

Example 1

Input:
[3, 4, 5]

Processing:
3! = 6
4! = 24
5! = 120

Output:
[6, 24, 120]
Sum = 150
Max = 120
Even Count = 3
'''

n = int(input('Enter the size: '))
print("plz enter ele...")

arr = []
for i in range(n):
    arr.append(int(input()))
print(arr)

fact = []

for num in arr:
   f = 1
   for i in range(1,num+1):
      f =  f*i
   fact.append(f) 
print(fact)

sum = 0
for i in fact:
   sum += i
print("Sum: ",sum)

max = fact[0]
for i in range(1,len(fact)):
    if fact[i] > max:
        max = fact[i]
print("Max: ",max)

even_count = 0
for i in fact:
   if i % 2 == 0:
       even_count += 1
print("Even Count: ",even_count)









