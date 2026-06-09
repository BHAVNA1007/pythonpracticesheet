'''
1
1 2
1  3
1   4
1  3
1 2
1
'''

n = int(input('Enter a number: '))
i = 1
while i<=n:
   print()

   j = 1
   while j<=i:
      if j==1 or i==j:
         print(j,end='')
      else:
         print(' ',end='')
      j += 1
   i += 1

i = n-1
while i>=1:
   print()
   j = 1
   while j<=i:
      if j==1 or i==j:
         print(j,end='')
      else:
         print(' ',end='')

      j += 1
   i-=1  
 

 

   
   