'''
*9. Check All Digits Are Even*
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to *check whether all digits of a number are even using loops*.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even
'''
num = int(input("Enter a number = "))
even = True 
while num > 0:
  last = num % 10 
  
  if last % 2 != 0:
     even = False
  num = num // 10 

if even:
    print("All Even")
else:
    print("Not All Even")

