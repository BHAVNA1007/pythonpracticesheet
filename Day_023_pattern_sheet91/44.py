'''

    1
   22
  333
 4444
55555

'''
n = int(input("Enter a number: "))

i = 1

while i <= n:

   print()

   space = 1
   while space <= n-i:
      print(" ",end='')
      space += 1

   j = 1
   while j <= i:

      print(i,end='')
      j += 1
   i += 1 

   
    
