'''
29) Diagonal Number Square
    1 - - -
    - 2 - -
    - - 3 -
    - - - 4
'''
n = int(input("Enter a number: "))
i = 1

while i<=n :
   print()
   space = 2

   while space<=i :
      print("-", end =' ')
      space += 1

   j = i
   while j<= n:
      if j==i: 
         print(i, end=' ')
      else:
         print("-", end=' ')
      j += 1

  

   i += 1

    
    