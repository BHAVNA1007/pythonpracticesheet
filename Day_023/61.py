'''

    *
   ***
  *****
 *******
*********

'''
n = int(input("Enter a number: "))

i = 1

while i<=n:
   print()

   space = 1
   while space <= n-i:
      print(" ",end='')
      space += 1
  
   j = 1
   while j<=2*i-1:
      print("*",end='')
      j += 1
   i += 1   