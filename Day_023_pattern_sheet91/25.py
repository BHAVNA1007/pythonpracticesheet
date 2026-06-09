'''
5
54
543
5432
54321
'''
n = int(input("Enter a number: "))

i = 1

while i <= n:
   print()

   j = 1
   k = n
   while j<=i :
      print(k, end='')
      k -= 1  
      j += 1
     
   
   i += 1 