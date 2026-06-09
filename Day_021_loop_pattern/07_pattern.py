'''
7.
enter n6
   
    *
   **
  ***
 *****
*******
'''
n = int(input("Enter a number: "))

i = 1

while i <= n:
   print()
   space = 1
   while space <= n-i:
      print(" ",end="") 
      space += 1

   s = 1
   while s <= i:
      print("*",end=' ')
      s += 1
   i+=1
   
   