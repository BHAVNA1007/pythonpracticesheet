'''
3. Perfect Number Reward System

A gaming company rewards users if entered number is a Perfect Number.

(Perfect Number = sum of proper factors equals number)

Write a program using for-else loop to:

- Find sum of proper factors
- If sum equals number print Reward Unlocked
- Else print Try Again

Input:
6

Output:
Reward Unlocked
'''
num = int(input("Enter the number = "))

sum = 0
i = 1
while i < num // 2:
     if num %  i == 0:
         sum += i
     i += 1
     if num == sum :
        print("try Again")
        break
else:
     print("Reward Unlocked")





   
    