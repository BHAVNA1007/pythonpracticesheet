'''
3.Zero Detection & Early Termination System

A financial system scans transaction IDs digit by digit. If a digit '0' is found, the system immediately stops processing further digits for security reasons.

Write a program to:

Traverse each digit of the number from right to left
Display each digit processed before encountering 0
Stop the loop immediately when 0 is found using break
Count how many digits were processed before termination
If no zero is found, print No Zero Found

Use loops and break wherever required.

Input:
572049

Output:
Digits Processed: 9 4
Count = 2
Zero Found - Process Stopped

Input:
56789

Output:
Digits Processed: 9 8 7 6 5
Count = 5
No Zero Found
'''
num = int(input("Enter The number = "))
count = 0 
zero = False
digit = '' 
while num > 0 :

    d = num % 10
   
    if d == 0:
      zero = True
      break
    print(d, end=" ")
    num = num // 10
    count += 1
print("\nCount = ", count)

if zero:
    print("Zero Found - Process Stopped")
else:
    print("No Zero Found")
        
     
   

   


       
     

  