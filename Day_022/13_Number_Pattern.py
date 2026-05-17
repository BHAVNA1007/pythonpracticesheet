'''
13) Number X Pattern
    1   5
     2 4
      3
     2 4
    1   5
'''
n = int(input('Enter a number: '))
i = 1
while i<=n:
   print()
   space =1
   while space<=i:
      print(' ',end='')
      space += 1

   j = 1
   while j<=2*(n-i):
      if j==1 or j==2*(n-i):
         print(i,end='') 
      else:
         print(' ',end='') 
      j+=1
   i+=1
i = n-1
while i>=1:
   print()
   space =1
   while space<=i:
      print(' ',end='')
      space += 1

   j = 1
   while j<=2*(n-i):
      if j==1 or j==2*(n-i):
         print(i,end='') 
      else:
         print(' ',end='') 
      j+=1
   i-=1