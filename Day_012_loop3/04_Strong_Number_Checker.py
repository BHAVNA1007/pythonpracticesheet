'''
4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number
'''
num = int(input("Enter a number = "))

t_sum = 0
new_num = num
while num > 0:
     sum = 0
     fact = 1
     digit = num % 10
     for i in range(digit, 0, -1):
         fact = fact * i
     
     num = num // 10
     sum += fact
     print(sum)
     t_sum += sum
print(t_sum)
if t_sum == new_num:
    print("Strong Number")
else:
    print("Not Strong Number")
     
    

  