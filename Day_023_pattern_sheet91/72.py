'''
A B C D E
 A B C D
  A B C
   A B
    A
'''

n = int(input('Enter a number: '))

i = 1

while i<=n:
   print()

   space = 1
   while space<=i:
      print(' ',end='')
      space += 1
  
   j = 1
   ch = 65
   while j<=n-i+1:
       print(chr(ch),end=' ')
       j += 1
       ch += 1 
   i += 1 