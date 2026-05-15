'''

ABCDE
 ABCD
  ABC
   AB
    A

'''
n = int(input("Enter a number: "))

i = 1

while i <= n:
   print()

   space = 1
   while space <= i:
      print(" ",end='')
      space += 1


   j = 1
   ch = 65
   while j <= n+1-i:
      print(chr(ch),end='')
      ch += 1
      j += 1
   i += 1 
   
