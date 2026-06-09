'''
55555
4  4
3 3
22
1
'''

n = int(input("Enter a number: "))

i = 1
k = n
while i<=n:
   print()

   j = 1
   
   while j<=n:
      if i==1 or j==1 or j+i==n+1:
         print(k,end='')
      else:
         print(" ",end='')
      j += 1
   k -= 1
   i += 1
          
         