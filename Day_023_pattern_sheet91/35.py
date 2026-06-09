'''
*****
*  *
* *
**
*
'''
n = int(input("Enter a number: "))

i = 1

while i<=n:
   print()

   j = 1
   while j<=n:
      if i==1 or j==1 or i+j==n+1:
          print("*",end='')
      else:
          print(' ',end='')
      j+=1
   i+=1  
        