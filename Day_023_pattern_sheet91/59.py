'''
    A
   A B
  A B C
 A B C D
A B C D E  
'''

n = int(input("Enter a number: "))

i = 1

while i<=n:
   print()

   space = 1
   while space <= n-i:
      print(' ',end='')
      space += 1

   j = 1
   ch = 65
   while j<=i:
      print(chr(ch),end=' ')
      ch += 1
      j += 1
   i += 1    