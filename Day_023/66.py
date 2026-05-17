'''
    1
   1*1
  1***1
 1*****1
111111111
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
   while j <= i*2-1:
       if i==n or j==1 or j==i*2-1:
           print("1",end='')
       else:
           print('*',end='')
       j += 1
   i += 1
 