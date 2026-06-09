'''
5 5 5 5 5
 4 4 4 4
  3 3 3
   2 2
    1
'''

n = int(input('Enter a number: '))

i = 1
k = n
while i<=n:
   print()

   space = 1
   while space <= i:
       print(' ',end='')
       space += 1
   
   j = 1
   while j<=n-i+1:
      print(k,end=' ')
      j += 1
      
   k -= 1
   i += 1    