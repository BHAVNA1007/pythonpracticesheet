'''
    1
   11
  1*1
 1**1
11111

'''

n = int(input("Enter a number: "))

i = 1

while i<=n:
   print()

   space = 1
   while space<=n-i:
      print(' ',end='')
      space += 1

   j = 1
   while j<=i:
      if i==n or j==1 or i==j:
          print("1",end='')
      else:
          print('*',end='') 
      j += 1
   i += 1
     
    