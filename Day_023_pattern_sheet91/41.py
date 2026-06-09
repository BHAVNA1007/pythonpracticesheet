'''

A
BCD
EFGHI
JKLMNOP

'''
n = int(input("Enter a number: "))

i = 1
ch = 65 
while i <= n:
   print()
   
   j = 1
   while j <= i*2-1:

       print(chr(ch),end="")

       ch += 1
       j += 1
   i += 1 

      