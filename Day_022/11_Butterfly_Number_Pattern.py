'''

11) Butterfly Number Pattern
    1      1
    12    21
    123  321
    12344321
    123  321
    12    21
    1      1
'''
n = int(input("Enter a number: "))
i = 1
while i<=n:
   print()
   j = 1
   while j<=i:
      print(j,end='')
      j+=1
  

   space=1
   while space<=2*(n-i):
      print(' ',end='')
      space+=1

   
   k = 1
   while k<=i:
      print(i,end='')
      k+=1
   i+=1

i = n-1
while i>=1:
   print()
   j = 1
   while j<=i:
      print(j,end='')
      j+=1
  

   space=1
   while space<=2*(n-i):
      print(' ',end='')
      space+=1

   
   k = 1
   while k<=i:
      print(j,end='')
      k+=1
   i-=1

