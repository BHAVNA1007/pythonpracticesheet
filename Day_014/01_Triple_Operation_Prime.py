'''1. Triple Operation Prime Verification System

A cybersecurity company generates a security score from entered access code.

Write a program to:

- Find sum of digits of the number
- Reverse the number
- Find absolute difference between original number and reverse
- Add digit sum and difference
- Check whether final result is Prime or Not Prime

Input:
4215

Output:
Sum of Digits = 12
Reverse = 5124
Difference = 909
Final Result = 921
Not Prime
'''
import math
num = int(input("Enter a number = "))

sum = 0
rev = 0
original_num = num

while num > 0:
   digit = num % 10
   sum = sum + digit
   rev = rev * 10 + digit
   num = num // 10

print("Sum of Digits = ", sum)
print("Reverse = ", rev)
diff = abs(original_num - rev)

print("Difference = ", diff)

f_result =  sum + diff

print("Final Result = ", f_result)

if f_result <= 1:
     print("Not prime")
else:
     for i in range(2,  int( math.sqrt(f_result))):
         if f_result % i == 0:
             print("Not Prime")
             break
     else:
          print("Prime")
   
 
         
    


