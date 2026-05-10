'''10.Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime
'''
import math
num = int(input("Enter a number = "))

original_num = num
sum = 0
zeros = 0
s_digit = 9
while num > 0:
    digit = num % 10
    if digit < s_digit :
        s_digit =  digit
    sum += digit
    if digit == 0:
        zeros += 1
    num = num // 10
print("Zero Count = ", zeros)
print("Sum = ", sum)
print("Smallest Digit =", s_digit)

final_result = original_num * s_digit

print("Final Result = ",final_result )



if final_result <= 1:
     print("Not Prime Number")

else:
     x = 0
     i = 2
     
     while i <= math.sqrt(final_result) :
         if final_result % i == 0 :
             x = 1
             break
         i+= 1
        
     if x == 0 :
         print(" Prime  " )
     else:
         print("Not Prime Number") 
        

