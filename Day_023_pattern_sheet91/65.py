'''
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
'''
n = int(input('Enter a number: '))
i = 0
while i<=n:
   print()

   space = 0
   while space <= n - i - 1:
      print(' ',end='')
      space += 1

   j = 0
   k = 1
   while j<=i:
      print(k,end=' ')
      k = k*(i-j)//(j+1)   
      
      j += 1
   k += 1 
   i+=1 
       