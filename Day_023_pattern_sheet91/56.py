'''

11111
 2222
  333
   44
    5
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
      print(i, end='')
      j += 1

   i += 1