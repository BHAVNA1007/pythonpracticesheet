'''
    A
   B B
  C   C
 D     D
EEEEEEEEE

'''
n = int(input('Enter a number: '))

i = 1
ch = 65
while i<=n:
   print()

   space = 1
   while space<=n-i:
      print(' ',end='')
      space += 1
   
   j = 1
   while j<=i*2-1:
      if i==n or j==1 or j==i*2-1:
         print(chr(ch),end='')
      else:
         print(' ',end='')
      j += 1
   ch += 1
   i += 1