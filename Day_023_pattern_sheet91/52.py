'''
12345
 1__4
  1_3
   12
    1
'''

n = int(input("Enter a number: "))

i = 1

while i <= n:
   print()

   space = 1
   while space<=i:
      print(" ",end='')
      space += 1

   j = 1
   while j<=n-i:
      if j==1 or j==n-i or i==1:
          print(j,end='')
      else:
          print("_",end='')
      j += 1
   i += 1 