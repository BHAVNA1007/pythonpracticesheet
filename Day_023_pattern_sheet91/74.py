'''
123456789
 1     7
  1   5
   1 3
    1

'''
n = int(input('Enter a number: '))

i = 1

while i<=n:
   print()

   space = 1
   while space <= i:
      print(' ',end='')
      space += 1
   
   j = 1
   while j<=n*2-i*2+1:
      if i==1 or j==1 or j==n*2-i*2+1:
          print(j,end='')
      else:
          print(' ',end='')
      j += 1
   i += 1


  