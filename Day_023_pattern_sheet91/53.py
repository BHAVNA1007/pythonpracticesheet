'''
55555
 4__4
  3_3
   22
    1

'''

n =int(input("Enter a number: "))

i = 1
k = n
while i<=n:
   print()

   space = 1
   while space <= i:
      print(" ", end='')
      space += 1

   j = 1
 
   while j <= n-i:
      if i==1 or j==1 or j==n-i:
          print(k,end='')
      else:
          print("_",end='')
      
      j += 1
   k -= 1 
   i += 1

   