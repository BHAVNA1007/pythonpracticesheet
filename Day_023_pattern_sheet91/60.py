'''

    X 
   X X 
  X__X
 X____X
X X X X X

'''
n = int(input('Enter a number: '))

i = 1

while i<=n:
   print()

   space = 1
   while space <= n-i:
      print(' ',end='')
      space += 1
   
   j = 1
   while j<=i:
      if i==j or i==n or j==1:
         print("X",end=' ')
      else:
         print("_",end=' ')
      j += 1
   i += 1 
           