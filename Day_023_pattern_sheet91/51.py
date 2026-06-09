'''

55555
 4444
  333
   22
    1

'''

n = int(input("Enter a number: "))

i = 1
k = n 
while i <= n:
   print()
   
   space = 1
   while space <= i:
      print(" ",end='')
      space += 1

   j = 1
   while j <= n+1-i:
      print(k, end="") 
      j += 1
   k -= 1
   i += 1 
   