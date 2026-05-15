'''

EEEEE
DDDD
CCC
BB
A

'''
n = int(input("Enter a number: "))

i = 1
ch = 69
while i <= n:

   print()
   
   j = i
   while j <= n:

      print(chr(ch), end = '')
      
      j += 1

   ch -= 1
   i += 1 

   
