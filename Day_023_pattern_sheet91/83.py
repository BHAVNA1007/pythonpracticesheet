'''

*        *
**      **
***    ***
****  ****
**********
'''
n = int(input('Enter a number: '))
i = 1
while i<=n:
   print()
   j = 1
   while j<=i:
      print("*",end='')
      j+=1
  

   space=1
   while space<=2*(n-i):
      print(' ',end='')
      space+=1

   
   k = 1
   while k<=i:
      print("*",end='')
      k+=1
   i+=1
