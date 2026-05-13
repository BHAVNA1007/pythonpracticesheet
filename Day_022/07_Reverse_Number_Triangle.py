'''
7) Reverse Number Triangle
    - - - -
    2 - - -
    4 3 - -
    6 5 4 -
    8 7 6 5
'''
n = int(input("Enter a number: "))
i = 1
k = 2
while i<=n :
   print()
   j = 2

   while j<=i :
      print(k, end =' ')
      j += 1
      k += 1 

   dsh = i
   while dsh<= n:
      print("-", end =' ')

      dsh += 1

   i += 1