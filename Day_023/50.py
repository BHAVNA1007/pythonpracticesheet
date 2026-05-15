'''
12345
 1234
  123
   12
    1
'''
n = int(input("Enter a number: "))

i = 1

while i <= n:
   print()

   space = 1
   while space <= i:
      print(" ", end='')
      space += 1

   j = 1
   while j <= n+1-i:
      print(j,end='')
      j += 1

   i += 1
       
   