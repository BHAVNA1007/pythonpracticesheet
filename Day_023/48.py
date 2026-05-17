'''
    A
   AB
  A_C
 A__D
ABCDE

'''

n =int(input("Enter a number: "))

i = 1

while i<=n:
   print()

   space = 1
   while space <= n-i:
      print(' ',end='')
      space += 1

   j = 1
   ch = 65
   while j<=i:
      if i==n or j==1 or i==j:
          print(chr(ch),end='')

      else:
          print("_",end='')
      j += 1
      ch += 1
   i += 1 


