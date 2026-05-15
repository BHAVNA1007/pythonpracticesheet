'''

*****
####
***
##
*

'''

n = int(input('Enter a number: '))

i = 1

while i <= n:

   print()

   j = i
   while j <= n:

      if i % 2 == 0:
          print("#", end='')

      else:
          print("*", end='')

      j += 1
   i += 1 