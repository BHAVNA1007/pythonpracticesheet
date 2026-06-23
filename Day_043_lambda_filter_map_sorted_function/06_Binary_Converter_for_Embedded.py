'''
06 Binary Converter for Embedded System

An embedded systems company develops microcontrollers that understand only binary values. Engineers enter decimal numbers, and the software must convert them into binary before sending them to the device.

As a software developer, write a recursive program to perform this conversion.

Task

Write a recursive function to convert a decimal number into its binary representation.

Input
Enter a decimal number:
25
Output
Binary Number = 11001

Note: Do not use Python's built-in bin() function.
'''

def bin_num(n):
    if n <= 1:         
       return str(n)

    return bin_num(n//2) + str(n%2)  

def main():
    n = int(input("Enter decimal Number: "))
    print("Binary is: ", bin_num(n))
 
main() 
           
   
