'''
1. Utility Toolkit System

You are developing a Utility Toolkit Application for a small office. Employees use this tool to quickly perform common number operations like checking prime numbers, reversing numbers, etc.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Check Prime Number
2 → Check Palindrome Number
3 → Reverse a Number
4 → Count Digits
5 → Exit

Sample Run 1:
Input:
Enter your choice: 1
Enter number: 7

Output:
7 is a Prime Number

Sample Run 2:
Input:
Enter your choice: 2
Enter number: 121

Output:
121 is a Palindrome Number

Sample Run 3:
Input:
Enter your choice: 3
Enter number: 456

Output:
Reversed Number is: 654

Sample Run 4:
Input:
Enter your choice: 4
Enter number: 98765

Output:
Total digits: 5

Sample Run 5 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

Sample Run 6 (Exit):
Input:
Enter your choice: 5

Output:
Exiting program... Thank you!
'''



import math
while True:
    print("Menu Options:")
    print("1 → Check Prime Number")
    print("2 → Check Palindrome Number")
    print("3 → Reverse a Number")
    print("4 → Count Digits")
    print("5 → Exit")
    choice = int(input("Enter your choice: "))
    match choice:
              case 1:
                   num = int(input("Enter The Number : "))
                   if num <= 1:
                         print("Not a Prime") 
                   else:
                        for i in range(2, int(math.sqrt(num))):
                             if num % i == 0:
                                  print("Not a prime")
                                  break
                        else:
                             print("Prime Number")
              case 2:
                    num = int(input("Enter The Number : "))
                    original_num = num 
                    l = len(str(num))
                    rev = 0
                    for i in range(l):
                          digit = num % 10
                          rev = rev*10 + digit
                          num = num // 10
                    if original_num == rev:
                          print(rev, ": is pelindrome Number") 
              case 3:
                    num = int(input("Enter The Number : "))
                    
                    l = len(str(num))
                    rev = 0
                    for i in range(l):
                         digit = num % 10
                         rev = rev * 10 + digit
                         num = num // 10
                    print(" Reverse a Number is :", rev)
              case 4:
                    num = int(input("Enter The Number : "))
                    l = len(str(num))
                    count = 0
                    for i in range(l):
                         digit = num % 10
                         count += 1
                         num = num // 10
                    print("Count Digits is :",count)   
              case 5:
                    print("Invalid Choice. Please try again.")
                    break
print("Exiting program... Thank you!") 

                    
              
                       
                    
                    
     














