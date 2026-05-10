'''
8.
enter n6
 654321
  65432
   6543
    654
     65
'''
n = int(input("Enter a number: "))

i = 1
while i <= n-1:
   print()
   space = 1
   while space <= i:
      print(" ",end="")
      space += 1

   j = i
   k = n
   while j<=n:
      print(k,end="")
      k -= 1
      j+=1
   i += 1
   