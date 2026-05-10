'''4.Spy Number Detector

A cybersecurity system flags special numeric codes.

A number is called a Spy Number if:
Sum of digits = Product of digits

Write a program to check whether the entered number is Spy Number or Not.

Input:
1124

Output:
Spy Number
'''
num = int(input("Enter the number = "))
l = len(str(num))
sum = 0 
product = 1
for i in range(l):
     d= num %10
     sum +=d 
     product *= d
     num = num //10
if sum == product:

    print("Spy Number")

else:

    print("Not Spy Number")
     
     


